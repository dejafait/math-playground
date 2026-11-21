# Whole-edge attempt, step152 — saved before execution

Approved target and source coverage: the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-10-physical-time-edge-paid-reserve-150.md`.
Exactly one whole-edge pass, no subdivision, time sweep or installation.
Inputs: L960 (definitions, uniform audited M32 and conditional payment),
L962 (independently audited corner F). Main gap remains L030–L032/C032a.

Set a=98/625, b=1/5, X=6000000185827 and I=[a,b]. First certify
X/(4pi)+a/16-N^2>0 and (N+1)^2-X/(4pi)-b/16>0 for N=690988.
Failure stops before finite differentiation. With s=(1+iX)/2 fixed,
the principal logarithm stays off its cut and alpha,alpha' are constant.
For u_n=log n write

    z_n(t)=exp(-s*u_n+t*(u_n^2/4-alpha*u_n/2)),
    beta_n=u_n^2/4-alpha*u_n/2,
    A'=sum beta_n*z_n, L'=sum u_n*beta_n*z_n,
    ell=2Re(alpha)+t Re(alpha*alpha'), ell'=Re(alpha*alpha'),
    S=ell*A-2L, S'=ell'*A+ell*A'-2L',
    F'=Re(conj(A')*S+conj(A)*S').

These identities are finite after the support gates. In particular both
amplitude and physical phase are differentiated, and n=1 gives z_1=1,
beta_1=0 exactly. All are C1 in real t; no moving cutoff or limit enters.
Using Rump2010 Theorem13.1 as assessed, an inclusion D for F'(I) gives
F(I) contained in F(a)+D*[0,b-a]. Independently bound R=|A| above by
the square root of the sum of squared component absolute upper bounds;
this requires no nonvanishing and no modulus differentiation. The existing
payment is E=p*(25R+81/2)+qR+pq, with p,q exactly as in L962.

Planned implementation reuses the L962 included dyadic operations and
finite elementary series at the whole interval input. Each prime phase
reduction must check its whole reduced interval is in (-4,4); composite
phases use the included multiplicative identity. All complete sums and
derivatives receive consecutive block records. No cancellation is assumed
between different interval occurrences. Width is physical and can be large.

Positive test: strict rational lower bound for F(a)+D*[0,b-a]-E_upper>0.
An unpaid range is inconclusive, not a negative paid sign or RH evidence;
it stops this enclosure mechanism for reassessment. Actual analytic,
remainder, companion and gauge hypotheses, spatial signs, seams, global
and zero-time transfer and actual-Xi positivity remain unresolved.
Execution and final canonical evidence were pending when this note was saved.
Mathlib match unchecked.

## Completed disposition

The full one-pass run finished with INCONCLUSIVE_WIDTH. The canonical
inclusion proof, exact rational comparisons, certificate paths and
qualifications are in L963. All 690988 terms and 338 blocks completed;
1056 separate endpoint checks passed. No positive or negative physical
sign was established. Preserve this pre-execution reasoning; stop the
rectangular derivative mechanism and assess any replacement separately.
