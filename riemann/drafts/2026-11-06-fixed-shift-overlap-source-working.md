# Indexed fixed-shift overlap: source-review working record

Literature-only review of the exact saved target in
`literature/2026-11-06-fixed-shift-certified-overlap-test.md`.
No mathematical computation, PF enlargement or overlap is established.

The full L836 statement and input interface were read, together with
L832, the relevant L834 simplicity/count passages, the ready finite-PF
assessment and the step659/667 stop records. The target changes neither
the quotient nor k=6002, J=6003, exact midpoint R, nor s=(1+q)/2.

Source leads now inspected:

- Arb 2.23.0 `acb_dirichlet.html`, “Riemann zeta function zeros”, states
  indexed isolation/refinement contracts, Rosser range 1..13999526,
  Turing range n>=2 and multiplicity-counted N(t). The matching FLINT
  v3.3.1 documentation source is accessible. These are algorithms with
  index guarantees, not unindexed decimal tables.
- python-flint tag 0.8.0 `src/flint/types/acb.pyx`, `zeta_zero`, forwards
  the positive integer and working precision to `acb_dirichlet_zeta_zero`.
  Its `arb.pyx` supplies directed lower/upper endpoints and exact dyadic
  mantissa/exponent export. The wrapper and exact endpoint contract are
  being compared with the relevant native implementation cases.
- Michałowski 2607.16795v1 Section1.2 restates m+1<=pi H for the
  finite-sector import; reuse L832's Katkova theorem and fixed-minor
  limit. Do not prove or claim the proposed numerical order in this turn.

Availability checks only: default Python3.15.2 has no installed
python-flint package. Python3.13/3.12/3.11 executables and uv exist.
No package installed and no zero or inequality evaluated. A future run
must record its actual package/native versions and preserve a setup
failure as a failure, rather than substitute mpmath or printed midpoints.

Completed: inspected the native Rosser block loop, dispatcher, indexed
isolation/refinement path and real-part assignment. The final source
comparison and precise execution obligations are saved in the assessment
named above, now SPECIALIZE. No global RH assumption is licensed by a
routine returning real part1/2. Python3.13 also has no package metadata;
an isolated, version-checked setup remains unpaid, not a source blocker.
