# Fixed full-first cumulant comparison — working step395

Approved target remains the unchanged assessment's fixed r=3,m=5
COVERED_TARGET. Reuse its EXPLORE coverage; no new source claim or
all-order mechanism is being approved. L019 supplies exact K/B and
decay; L767 supplies the normalization, signed finite differences and
the effective x>=131072 tail. Its independent audit remains pending.

Main gap: actual-Xi all-degree positivity. Intermediate target: finish
the signed base/relative-error comparison on the remaining compact
range, including u=0. It could support actual cumulant reverse
regularity; higher orders and exceptional coefficient transfer remain
unresolved. Continue only with rigorous positive base and relative
error <1/2. Negative certified values stop this parameter choice;
samples or failed enclosures do not. Persistent cancellation failure
after this refined attempt requires reassessment.

Existing changes are extensive and preserved. Read L019/L767 and the
step394 working note, scripts and history; checked the narrowly relevant
November4 cumulant failure note. It concerns a different-kernel direct
transfer, not this actual full-first-summand comparison. Literature
overlap is already assessed in the supplied review and is reused.

Plan being tested: sharpen the large-x Taylor enclosure, then use
certified moment integration and local Taylor polynomials for the
compact determinant. Retain cancellation before taking absolute
remainder bounds. Any computed certificate needs analytic remainder,
all-summand and continuum control; a finite grid is insufficient.

## Completed result and remaining work

L768 now records the full fixed-domain comparison. A degree-20
epsilon expansion reduces the unbounded tail to x>=32. Certified
degree-36 panel integration and degree-64 local Taylor models cover
all 29 closed cells from x=3 to x=32, hence the endpoint x=pi.
The signed determinant polynomial is formed before interval evaluation.
The complete n>=2 remainder is bounded by gradient estimates, with
n=2 explicit and all n>=3 included in an analytic majorant.

The final certificate is scripts/cumulant-comparison/compact-certificate-395.json.
It gives s(d)>1/(10x^3) and relative error<37/100<1/2 on the whole
required domain. It records all panel, coefficient, remainder and cell
evidence. The earlier first-cell certificate is retained. No failed
compact enclosure or negative discriminator arose. Exact formulas,
analytic hypotheses and software rounding qualifications are canonical
in L768; no all-order extrapolation is made here.

Unfinished work is the independent audit of L767/L768 and the complete
certificate, especially the complex analytic remainder bounds and
the interval computation. Higher-order smoothing, exceptional
coefficient transfer and actual-Xi all-degree positivity remain open.
The next audit target is nominated with REVIEW_REQUIRED; this turn
does not approve new mathematics or perform its own independent audit.
