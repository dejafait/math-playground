# Signed angular mean of the paired residual — working step 46

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-02-displaced-positive-cone-distance.md`.
The exact target is its unchanged rate-1/100 nonnegative cone distance.
This bounded subtest evaluates the actual zeroth angular Fourier
coefficient of C673d's explicit positive residual, using L666 and L673.
Actual-Xi all-degree signs, the uniform cone bound, the unit-residue
application, support and realization remain independent gaps.

Test: a proved lower bound |m_n| >= exp(-alpha*n)*n^(-C), alpha<1/100,
along unbounded q would rule out this particular approximant, by
Cauchy--Schwarz on normalized angular measure. It would not lower-bound
the infimum over all positive coefficients. A small or zero mean proves
no norm upper bound. Park the scalar test if it yields neither a
discriminating bound nor a controlled signed-norm mechanism.

The previously read C673d Section 1 checks out for the needed branch and
signs: the linear-factor roots lie outside |Re z|<109/404; principal
logarithms define an even nonzero fourth root, positive on the imaginary
axis. The phase-node identity in L673 makes ell_k*g_n(+-i*y_k)<0.
This is not an audit of C673d's crossing certificate.

## Reasoning saved before computation

Write J=n-1 and p_j=t_j*x/U. L666 gives

    W_a(u)=(x/a) product_(l=1..J)
             [(x-t_l*u)/(a-t_l*u)] [(U*u-t_l*a)/(U*u-t_l*x)].

Its only interior candidate poles are the distinct p_j, while all
a/t_l lie outside the unit circle. W_a is regular at zero, W_a(0)=x/a.
Applying the residue theorem to W_a(u)/u should give its true angular
mean as x/a plus the J interior residues; cancellation at a candidate
pole is allowed. With no omitted j=0 factor, the proposed residue is

    R_j(a)=(x-a)/a
       *product_(l=1..J) (x-t_l*p_j)/(a-t_l*p_j)
       *product_(l!=j) (t_j*x-t_l*a)/(x*(t_j-t_l)).

For conjugate pairs, the mean is real and equals

    m_n=1+2*sum_k b_k*Re[x/a_k+sum_j R_j(a_k)], a_k=x+i*y_k.

Verify this finite formula algebraically and compare its numerical
evaluation with independent angular integration at small q. Numerical
precision comparisons and finite rates are diagnostics, not rigorous
asymptotic bounds or certificates for the cone target. Preserve all
signed terms. No fresh source-dependent theorem is needed beyond the
standard named residue theorem already covered by the assessment.

## Completed bounded calculation

The needed identity was found already in C645o equation (4), specialized
to its second argument x. C673d Section 5 now contains the specialization,
all pole checks, the conjugate-pair simplification and the precise
Cauchy--Schwarz qualification. No new lemma or general identity was needed.
The full expression was implemented using standard-library Decimal because
the available Python has no mpmath; no package installation was attempted.

The complete diagnostic is
`scripts/one-sided-hankel/positive-cone-angular-mean-screen.json`.
For n=15,27,51,99,195 the computed means are approximately
2.07389446105, -0.573467966686, -0.249033956595, -0.0933167985947,
and -0.0115556350477. Precision 80/140 differences are <2.4e-42;
the small-q direct angular integrations agree within 1.4e-15. These
are diagnostic observations, not enclosures or asymptotic evidence.
No norm bound or cone discriminator follows. Outcome EXPLORATION,
classification REPRODUCTION; park this scalar route.

Qualification to the initial test: a lower bound only on one unbounded
subsequence excludes these coefficients only on that subsequence. It
does not rule out another subsequence, nor bound the cone infimum.

The new proposal prescribes a positive-real action on the entire allowed
vertical interval and asks for a small angular representer. This is a
different observation mechanism, independent of displacements, rather
than another scalar-mean evaluation. The associated primary theorem
coverage is missing; `drafts/literature/2026-11-02-positive-real-angular-separator.md`
is REVIEW_REQUIRED. No construction, norm estimate or approval of that
new target was performed. The sole next action is in PROGRESS.md.
