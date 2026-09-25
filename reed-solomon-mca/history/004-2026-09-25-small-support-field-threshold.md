# 004 — 2026-09-25 — Small-support certificates and field-size scope

Performed one interpolation/counting step after reading the required files and
preserving existing changes. The
[saved test](../drafts/2026-09-25-small-support-field-threshold.md) names the
gap, intermediate target, downstream use, redundancy check, and continuation
test. The [official statement](https://proximityprize.org/) and
[paper metadata](https://eprint.iacr.org/2026/680) were reread; the source bridge
remains uncertified, and unsuccessful PDF retrieval was not repeated.

[L003](../lemmas/L003-rs-small-support-field-threshold.md) extends the
constant-code count to every RS dimension below the length. It supplies the
all-radius upper bound N/q, with N=binomial(n,k+1), and proves equality at
terminal radii if q > binomial(N,2). The full proof uses interpolation and
avoiding finitely many hyperplanes. No earlier lemma is used as a premise;
the new DAG row consequently has no lemma inputs, and previous rows remain.

The distinction between a certificate and an admissible support is essential:
the smaller support need not meet the original radius's size threshold. The
count gives an upper bound there, with the exact event asserted only at
terminal radii. The extra hypothesis for sharpness is also kept separate from
the sufficient safety threshold. The result quantitatively delimits eventual
field-size safety beyond dimension one, including all four rates on a smooth
length-16 domain at error 2^-128. It does not solve the sharp radius at general
q; at length 256 and rate 1/2 its sufficient threshold exceeds 2^379.

Outcome: ADVANCE, a relevant mathematical input for the pinned model, with
exploration turns reset to zero and STATUS kept IN_PROGRESS. There is no
complete challenge candidate. The reason for the subsequent direction is that
a large support may force many small certificates for the same challenge;
counting this multiplicity could retain radius information lost by the plain
union bound. The sole current action is in PROGRESS.md.

Validation: `python3 scripts/small-support/check.py` passed 16,369 input-pair
classes modulo code translations across six small parameter sets, all supports
and challenges, a ten-root F_101 witness, and exact threshold comparisons.
The enumeration is auxiliary to the general proof. The source correspondence,
radius-size qualification, and additional sharpness condition were reviewed
directly rather than inferred from these finite checks.

`python3 ../scripts/docs/check_structure.py --problem reed-solomon-mca`
passed with 4 nodes, 1 edge, valid links, and compact overviews;
`git diff --check -- .` also passed. Structural validation does not certify
the mathematics or the paper-to-model correspondence.
