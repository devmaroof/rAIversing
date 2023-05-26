import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
MODULES_ROOT = os.path.join(REPO_ROOT, "modules")
PROJECTS_ROOT = os.path.join(REPO_ROOT, "projects")
EVALUATION_ROOT = os.path.join(PROJECTS_ROOT, "Evaluation")
EVAL_P2IM = os.path.join(EVALUATION_ROOT, "p2im")
TESTING_ROOT = os.path.join(REPO_ROOT, "testing")
SAMPLES_ROOT = os.path.join(TESTING_ROOT, "samples")
BINARIES_ROOT = os.path.join(SAMPLES_ROOT, "binaries")
P2IM_BINS_ROOT = os.path.join(BINARIES_ROOT, "p2im")
P2IM_ORIG_BINS = os.path.join(P2IM_BINS_ROOT, "original")
P2IM_STRIPPED_BINS = os.path.join(P2IM_BINS_ROOT, "stripped")
P2IM_NO_PROP_BINS = os.path.join(P2IM_BINS_ROOT, "no_propagation")
GHIDRA_ROOT = os.path.join(MODULES_ROOT, "ghidra")
GHIDRA_SCRIPTS = os.path.join(GHIDRA_ROOT, "ghidra_scripts")
AI_MODULES_ROOT = os.path.join(MODULES_ROOT, "rAIversing", "AI_modules")


#TODO: fill in the following to match your ghidra installation
GHIDRA_INSTALL_DIR = os.path.join(GHIDRA_ROOT, "ghidra_10.2.2_PUBLIC")
GHIDRA_HEADLESS_BINARY = os.path.join(GHIDRA_INSTALL_DIR, "support","analyzeHeadless")

