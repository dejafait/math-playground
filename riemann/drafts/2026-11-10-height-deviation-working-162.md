# Height/deviation finite witness — working checkpoint, step162

The exact approved target is the height/deviation-only degree bound in
the unchanged EXPLORE assessment `drafts/literature/2026-11-10-height-deviation-witness-degree-review-157.md`.
Main gap: actual-Xi all-degree L030 positivity. Intermediate target:
supply quantitative negative Li data for audited L964 from a hypothetical
zero at height <=T and deviation >=delta. Actual signs remain independent.

Scoped comparison reread L032/L895 and the direct-import stop; neither
removes its head-conditioning inputs. Palojarvi v2 Lemma 2.2 has been
rechecked: M complex numbers with maximum modulus 1 have a real power
sum >=1/20 at some integer k in [1,5M]. Repetitions are permitted.
No printed zero-count constants or Theorem 3.1 specialization is used.

Provisional mechanism, NOT YET VERIFIED: use w=rho/(rho-1), choose
R=sqrt(1+2delta/(T^2+1/4)), r=sqrt(R), and split at |w|>r.
A hypothetical reflected zero gives |w|>=R. The finite head has
M<=2A((R-1)^(-1)+1/4) by reciprocal-node mass A. Normalize the
head by its largest modulus and apply Lemma 2.2 to Nth powers.
For some n=Nk<=5MN its real power sum is >=R^n/20.
On the complete complement, Taylor expansion along [1,w] appears to
give |Re(1-w^n)|<=n^2 r^n/(Im rho)^2. Total reciprocal-ordinate
mass is <=(65/32)A by L026. Thus the candidate inequality is

    lambda_n <= M - R^n/20 + 3A n^2 r^n.

Continue only after proving this for every omitted zero, justifying
the real Li sum and an explicit actual-Xi mass bound A, then choosing
N to dominate both positive errors and supplying a uniform L964 degree.
Abandon this composition if any of those inequalities is unpaid.
This is unfinished reasoning, not a lemma or an accepted conclusion.

## Disposition after the bounded attempt

The provisional mechanism is now fully written, but not independently
audited, in canonical L965. The explicit actual-Xi mass is A_0<260/4473<1;
the full reciprocal-ordinate mass is <3. Setting B as the uniform head
bound, a=log(r), and N=ceil(max{1,40B/a,1440/a^3}) pays the head
and tail errors by 1/80 each after division by R^n. Thus a multiple
n of N, with n<=5BN, has lambda_n<=-R^n/40<=-1. L964 with
epsilon=A=1 gives the stated uniform D(T,delta) and Q(q)<-3/4.
All proofs and constants are canonical in L965, not duplicated here.
No actual negative coefficient or RH conclusion has been supplied.
The next use must first subject the new conditional bound to an
independent conceptual audit within the unchanged target and assessment.
