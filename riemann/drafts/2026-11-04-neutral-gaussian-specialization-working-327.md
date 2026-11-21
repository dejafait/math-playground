# Neutral Gaussian specialization — working record, step 327

The supplied SPECIALIZE assessment
`drafts/literature/2026-11-04-neutral-gaussian-domain-differentiation.md`
approves exactly the current target. This is a REPRODUCTION/calculation
step, not new source discovery or a sign theorem.

Main gap: unconditional complete neutral Weil positivity. Intermediate
target: the full-line Gaussian identity and two continuous time
derivatives on each bounded interval including right derivatives at zero.
Downstream use: make a later differential sign estimate meaningful.
Continue only if weighted moments, strip decay and all three complete
pairings admit uniform majorants; record and narrow any failed claim.
Independent starting sign and backward propagation remain unresolved.

Planned normalization: F(z)=integral f(x)exp(-izx)dx,
H_tau(z)=exp(-2 tau z^2)F(z)overline(F(conj(z))). The second factor
is reflected conjugation, hence holomorphic, not an absolute square
off the real axis. The spatial inverse transform is
c_tau=f_tau*tilde(f_tau)=G_(2tau)*(f*tilde(f)). Expect
partial_tau^j c_tau=2^j G_(2tau)*(f*tilde(f))^(2j).
Retain both pole evaluations until exact neutrality is proved.

Primary Lemma 4's full statement and Fourier convention were retrieved
to implement the already-reviewed specialization, not to refresh its
literature gate. Local L018 and L744(6)-(7) were read. Existing dirty
files and unfinished notebook work are preserved.

The candidate domination works on each fixed [0,T], T>0. If
supp(c) is contained in [-A,A], d=|x|-A>=1 and 0<s<=2T,
then

    G_s(x-y) <= (pi e)^(-1/2) exp(-d^2/(16T))

uniformly for |y|<=A: split its exponential into two equal factors
and use sup_(s>0) s^(-1/2)exp(-1/(8s))=2/sqrt(e).
For j<=2 this bounds 2^j G_(2tau)*c^(2j). At x=log n it
dominates the entire von Mangoldt sum, since its Gaussian in log n
eventually beats n^(-2). At zero, c and all its derivatives remain
compact; there is no positive-time cutoff.

Strip integration by parts for compact f gives arbitrary polynomial
decay of F(z) on each fixed strip; multiplication by exp(-2tau z^2)
and z^(2j) preserves a uniform rapid bound for tau in [0,T].
L024's reciprocal-square zero summability supplies the zero-side
majorant without assuming real ordinates or importing a zero count.
Both original exponential moments acquire only exp(tau/4), hence
remain zero. Canonical write-up is in preparation; these are working
calculations, not an independent audit or an asserted sign law.

Completed: the full argument is canonical in
`lemmas/L753-neutral-gaussian-complete-weil-identity.md`. L024 was
read in full for the required summability, with no new zero-count
input. The DAG records direct inputs L018/L024/L744. A separate
audit-coverage request remains REVIEW_REQUIRED; the identity supplies
neither of the unresolved sign inputs.
