---
id: pre-tool-hook-blocks-data-paths-for-remote-model
typ: befund
status: vorschlag
thema: knowledge/local_llm_operation
stand: 2026-10-17
herkunft: Hermes profile with the hub model as backend, Alita session 2026-10-16/17
verweist_auf: [remote-model-gets-only-data-free-skills-and-redacted-text]
---

# A pre-tool-call plugin is the hard barrier for a remote-model agent; a system-prompt rule alone is a request

## Aussage
1. With a remote model every tool result is sent to the remote server. A system-prompt rule ("never read patient data")
   was obeyed in tests, but is only a request to the model.
2. Hermes plugins can register `pre_tool_call` (return `{"action": "block", "message": ...}`) and `transform_tool_result`
   hooks. A user plugin in `$HERMES_HOME/plugins/<name>/` loads only when listed under `plugins: enabled:` in config.yaml.
   Test 2026-10-17: the agent was told explicitly to `ls` a data folder; the call was blocked and logged.
3. Side effect: redacting results that contain image-file endings (`.nii`) or `sub-` ids also hits ordinary code repos and
   docs; the agent then had to read files in small pieces. Patterns for case ids should be narrower than "sub-*".
4. Hermes "bare custom" endpoints read the key from `<VENDOR>_API_KEY` derived from the host (here CHARITE_API_KEY), not from
   `model.key_env`; a 401 is the symptom.

## Trägt
Plugin list (`hermes plugins list`: enabled), guard log line of the block, the agent's report on blocked reads.

## Trägt nicht
Prompt-injection or code that reads data without naming the path (e.g. a script that globs `~`) is not covered;
the result redaction is the second line there.

## Bruchindikator
A data path reaching the remote model despite the plugin (guard log empty while the session shows data).

## Ablesung
- Hermes Agent source: hermes_cli/plugins.py (`_dispatch_pre_tool_call_hooks`, plugin enable gate), plugins/security-guidance
  as reference plugin; hermes_cli/runtime_provider.py (`_host_derived_api_key`); repository commit f0daf56 (2026-09-02)
- own tests 2026-10-17
