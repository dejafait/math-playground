# Second Cauchy derivative — bounded replay working record

STEP_ID: 2026-10-31-associated-theta-cauchy-second-derivative-replay-01

Working only on the supplied SPECIALIZE target. The parent assessment's
duplicate/failure screen and primary shape input have been reused; no
third derivative or full hierarchy is being attempted.

Candidate calculation, to be checked and placed in a canonical lemma:
put c(y)=C_A(iy). Evenness gives
c(y)=(1/pi) integral_0^infinity A(t)y/(t^2+y^2) dt.
Integration by parts with arctan(t/y) gives
c(y)=-(1/pi) integral_0^infinity A'(t)arctan(t/y) dt.
The endpoints vanish since A(infinity)=0 and arctan(0)=0.
Then c''(y)=-(2y/pi) integral_0^infinity t A'(t)/(t^2+y^2)^2 dt>0
if admissibility supplies A'(t)<0 and the compact-y domination holds.
The exact rescaling to check is A(t)=128 K_1(t/2;Phi), obtained from
k(u)=4 Phi(u/2) and s=2v. This is generic shape calculus, not a
theta-specific positivity mechanism.

Sign warning under independent replay: Norvidas 2009.04449v1 (2.15),
n=1, displays the opposite sign for u_f''(0,y)=2c_f''(y). Its (1.7)
at n=0 likewise asks for a nonnegative integral with f', whereas the
calculation above makes that integral negative for admissible f.
HTML exact formula and preceding integration-by-parts line were read;
PDF visual confirmation and complete endpoint/differentiation proof
remain before the final record. No general correction for other orders
or rejection of Theorem 2 is asserted.

Completed: canonical full proof and citations are now in L597. The
versioned PDF text at printed pp.3 and 6 confirms the signs in (1.7)
and (2.15); screenshot calls did not expose a viewable image, so no
visual inspection is claimed. Direct Poisson differentiation and one
integration by parts check both the formula and the endpoints; the
Gaussian check meets every hypothesis of the disputed corollary.
The original arctan scratch calculation is preserved above; the
canonical proof uses the direct rational derivative instead. No
third derivative, numerical test, mathematical script or full-hierarchy
claim was made. The finite shape-only target is complete.
