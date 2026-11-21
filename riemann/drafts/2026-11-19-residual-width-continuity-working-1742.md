# Residual width continuity attempt1742

19 November 2026. Research under the unchanged, separately approved
EXPLORE assessment1740. Supplied overview/DAG/checkpoint used directly;
all pre-existing changes are preserved. Main gap remains L030-L032/C032a
actual-Xi all-degree positivity. Target is exactly assessment1740's
continuity-at-1 test for C033i's residual law in C032q's finite signed
width range. No new target or literature review is being undertaken.

Inputs read: C032j in full; C032q through its signed construction and
positivity test; C033i in full; C032s heat-error/cancellation and endpoint
sections; C032u comparison scope; source-notes1740 and unfinished
working1740. Existing duplicate/failure assessment is reused.

Unfinished plan: write D_sigma=ell_sigma-ell_1 as
t^(-3/2)[K(u_sigma)-K(u_1)]. C032s's separately controlled heat errors
give |K'(u)|<=C/u near zero. Integrate over [u_sigma,u_1] to seek
|D_sigma(t)|<=C' t^(-1/2), uniformly in sigma in [1,2]. At infinity
K is evaluated in a common compact positive-time interval, giving
O(t^(-3/2)). Neither a sign of D_sigma nor a density of nu_sigma is
needed. These claims are not yet a completed result in this draft.

If these bounds hold, use the cited finite-signed-measure exponential
to construct R_sigma=exp(-M_sigma) E(D_sigma(t)dt). The atom at zero
must be retained. Euler beta bounds should control convolution densities
uniformly near 1; total-variation convergence by itself is insufficient.
Integrate against a fixed arbitrary finite |eta| without imposing a
common variation cap. Identify nu_eta=nu_1*R_eta on all Borel sets.
For a purported representation of C033i's mu, cancel the strictly
positive Laplace transform of nu_1 and use signed uniqueness via Jordan
parts, including zero, to identify R_eta=lambda.

Discriminator still to prove: lambda has density zero on (0,1) and
-exp(m)*ell_1 on (1,3/2), with ell_1 continuous and strictly positive
at 1. Equality of measures must force incompatible one-sided values
for the continuous density of R_eta, rather than compare chosen
pointwise representatives. Abandon this discriminator if a required
uniform bound, signed identification or representative comparison fails.
Full cancellation J_eta=0, moments/tails and actual-Xi realization are
independent gaps. No claim beyond the inspected literature is certified.

## Completed disposition

The test succeeded conditionally on the retained inputs. The full proof
is canonical in [C033j](../lemmas/C033j-residual-law-excluded-from-finite-signed-width-range.md).
It proves a uniform integrable width-difference envelope, uniform local
convolution-density convergence, all-Borel signed factorization and the
incompatible continuous representative at 1. No numerical certificate
or mathematical script was needed. Classification is POTENTIALLY_NEW
under EXPLORE1740, meaning only no matching result was established by
the reused search; it does not assert novelty beyond the literature.
The result awaits separate conceptual audit. The unfinished plan above
is retained as the checkpoint made before the lengthy proof.
