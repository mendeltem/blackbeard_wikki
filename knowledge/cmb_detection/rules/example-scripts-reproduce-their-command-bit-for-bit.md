---
id: example-scripts-reproduce-their-command-bit-for-bit
typ: regel
status: vorschlag
thema: knowledge/cmb_detection
stand: 2026-10-22
herkunft: Python examples of cmb_3d_unet_experiments (branch python-examples, commit 53b21a0), own runs 2026-10-22
verweist_auf: [fine-tune-from-public-valdo-weights, count-lesions-on-the-fine-grid-deliver-a-label-map]
---

# Example scripts that restate a pipeline must reproduce its command bit for bit

## Aussage
Readable example scripts (train, predict, fine-tune written out step by step) are only trustworthy if a test shows that
they compute what the package's own commands compute. With fixed seeds on the CPU that is an exact test, not a
tolerance:

1. **Weights equal with `torch.equal`, masks equal voxel for voxel.** Measured 2026-10-22: `01_train_unet.py` against
   `cmbx train --frst_from cmbx`, `03_fine_tune_unet.py` against `cmbx fine_tune --frst_from cmbx` (same weights, same
   held-out cases, same threshold and minimum size), `02_predict_microbleeds.py` against `cmbx evaluate` (same masks on
   the scan grid, same lesion counts).
2. **Equality needs the same order of random draws:** seed torch, then the numpy generator, then build the network,
   then the optimizer over the same parameter list, then the patch draws in the same order. Predicting the held-out
   cases draws nothing, so the script may evaluate at other epochs without changing the weights.
3. **Two empty masks prove nothing.** Keep one comparison with a model that finds lesions: the public VALDO model found
   88 and 69 voxels on the two synthetic phantoms, and the test asserts a count above zero.
4. **Copies stay copies:** scripts meant to be read alone repeat a few functions; a test compares their source text
   (`inspect.getsource`), so a fix in one cannot silently miss the other.
5. **Numbered top-level scripts with a process pool need the `if __name__ == "__main__":` guard** around the steps
   (spawn and forkserver re-import the main module); functions stay above it, tests load the file with importlib.

## Trägt
13 tests (about 90 s on 4 CPU threads, tiny network of width 8), full suite 322 green in a fresh environment.
The same scripts gave the same numbers on a second run in a new environment (held-out F1 0.133 and 0.100 at epoch 1
and 2, identical to the command).

## Trägt nicht
Bit equality holds for one machine and one PyTorch build on the CPU; on a GPU (bfloat16 autocast) and across releases
only closeness can be expected (PyTorch documentation). The from-zero check ran on the development workstation: a new
local environment, and a delegated "remote" agent that in fact ran on the same machine (GPU hidden, warm pip cache).
A truly fresh CPU-only machine is still open; such a check must first record host name and GPU, otherwise it does not
count as a fresh machine.

## Bruchindikator
A seed-for-seed rerun of script and command on the CPU that gives different weights, or a predict comparison whose
masks are all empty.

## Ablesung
PyTorch, "Reproducibility" notes (https://docs.pytorch.org/docs/2.14/notes/randomness.html, checked 2026-10-22):
completely reproducible results are not guaranteed across releases, commits or platforms, nor between CPU and GPU;
`torch.manual_seed` seeds the generator for all devices, and with other nondeterminism removed the same environment
gives the same numbers. Python, `multiprocessing`, "Safe importing of main module"
(https://docs.python.org/3/library/multiprocessing.html, checked 2026-10-22): with spawn or forkserver the main module
must import without side effects; protect the entry point with `if __name__ == '__main__':`; since Python 3.14
forkserver is the POSIX default. Code: https://github.com/mendeltem/cmb_3d_unet_experiments (examples/python,
tests/test_python_examples.py). Own runs 2026-10-22 on synthetic phantoms only.

## Verknüpft
[fine-tune-from-public-valdo-weights](../findings/fine-tune-from-public-valdo-weights.md),
[count-lesions-on-the-fine-grid-deliver-a-label-map](count-lesions-on-the-fine-grid-deliver-a-label-map.md)
