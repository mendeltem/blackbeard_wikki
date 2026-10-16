---
id: python-env-isolation-on-shared-clusters
typ: regel
status: getragen
thema: knowledge/agent_tooling
stand: 2026-10-16
herkunft: install tests of a public research package (cmb_3d_unet_experiments) on a workstation and an institute SLURM cluster, 2026-10-16
verweist_auf: [release-test-means-fresh-machine-with-release-assets, pip-freeze-is-not-an-install-file]
---

# A Python environment on a shared machine is only isolated if you make it so

## Aussage
Six failures, each seen once on 2026-10-16, each silent or misleading, and the fix that now sits in the install script:

1. **User site leaks into every environment.** Packages in `~/.local/lib/python3.X/site-packages` are on `sys.path` of
   every interpreter of that version, conda env or venv. On the cluster pip reported requirements as "already satisfied"
   from `~/.local` and printed pages of resolver errors for unrelated packages there. Reproduced: a fake `yaml` in a user
   site shadowed the environment's PyYAML 6.0.3. Fix: `export PYTHONNOUSERSITE=1` during the install AND in the
   activation script; the self-test reports any module loaded from the user site.
2. **conda on a login node.** Twice the SSH session died at exactly `Collecting package metadata (repodata.json)`
   (conda-forge index, several GB RAM while parsing); the same command on a compute node (srun, 128 GB) ran through.
   Fix: install on a compute node or in tmux; `--venv` (Python of the active conda base + pip, no conda download);
   the script falls back to a venv by itself when `conda create` fails.
3. **Ubuntu Python without `python3-venv`.** `python3 -m venv` fails (ensurepip missing), no sudo. Fix: `uv venv` if
   present, else `venv --without-pip` + `get-pip.py`.
4. **An editable install points to an old clone.** `python -m pkg` in a test loaded the package from a clone made the
   day before, so a whole option matrix first tested stale code. Fix: before any test print
   `python -c "import pkg; print(pkg.__file__)"`.
5. **`conda env remove` of the active environment is refused.** Fix: `env -u CONDA_PREFIX -u CONDA_DEFAULT_ENV conda env remove`
   inside the script (`--recreate`).
6. **`echo "$(date) rc=$?"` always logs rc 0** -- the command substitution runs first and resets `$?`. Fix:
   `rc=$?; echo "$(date) rc=$rc"`.

## Trägt
Every item reproduced and fixed with a test (fresh clone, empty environment, simulated failure).

## Trägt nicht
Says nothing about which Python versions or CUDA builds work; that is the job of the install matrix.

## Bruchindikator
A user reports resolver errors or "already satisfied" lines pointing outside the environment; a test log whose
module paths are not inside the environment.

## Ablesung
Python docs, `PYTHONNOUSERSITE` and the user site: https://docs.python.org/3/using/cmdline.html#envvar-PYTHONNOUSERSITE
and https://docs.python.org/3/library/site.html (Python 3.12). GNU Bash manual, Special Parameters (`$?`) and Command
Substitution: https://www.gnu.org/software/bash/manual/bash.html. conda docs, managing environments:
https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html. Measurements: install logs of
2026-10-16 (cluster login node vs compute node; workstation fresh-clone tests).

## Verknüpft
[release-test-means-fresh-machine-with-release-assets](release-test-means-fresh-machine-with-release-assets.md),
[pip-freeze-is-not-an-install-file](pip-freeze-is-not-an-install-file.md)
