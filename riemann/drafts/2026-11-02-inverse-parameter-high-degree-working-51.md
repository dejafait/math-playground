# Inverse-parameter high-degree attempt — step 51

Invocation-start target and EXPLORE assessment are unchanged:
`drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`.
Main gap: actual-Xi all-degree mixed positivity. The intermediate target
is the saved degree-at-most-n real polynomial action, all three values,
closed-segment real-part signs, exact exterior equality and cost
exp(n/100)*n^C. Its possible use is an angular positive-cone separator;
original unit residues, H, support and Xi realization remain independent.
Continue with a complete paid construction or a quantified restriction;
abandon only a class actually excluded by the evidence.

L675's full range proof and low-degree cost bound were read, along with
L666's complete rational identity and the step-50 history/stop. No
nonvanishing of higher beta coefficients or optimality of its displayed
inverse may be assumed. Existing notebook changes are preserved.

## Reasoning saved before further work

Rotate the angular coordinate to v=-u, so lambda*u=s*v, s=11/10.
Write b(z)=N(z)/D(z), h_j=t_j/R, and

    F(v)=b(s*v),
    I(v)=product_j (v-h_j/s)/(1-(h_j/s)*v),
    O(v)=s^J*product_j (1-(h_j/s)*v)/(1-h_j*s*v).

Then F=I*O, |I|=1 on the circle; O and its inverse are analytic
on a neighborhood of the closed disk. For a finite negative-frequency
polynomial g(v)=sum_(k=0)^J H_k*v^(-k), choose
conjugate(psi(-v))=I(v)*g(v). Its norm is exactly ||H||_ell2.
Here f=conjugate(psi(-v))/F=g/O has no Fourier indices below -J,
so L675's coefficient identity gives a polynomial action of degree<=n.
This is a potential sharper parametrization, not yet a sign/cost
construction or a claim to have classified all preimages.

At w=1 the coefficient functional should reduce to the first J+1
Taylor coefficients of I=b(s*v)/O(v). For other w the corresponding
functional is the truncated Taylor series of b(s*v*w)/O(v).
The value at w=10/11 and the entire closed ordinate arc must still be
enforced. Possible beta zeros do not obstruct this forward construction.
Full algebra, interchanges, uniform estimates and signs remain to check.

## Completed attempt and duplicate reconciliation

The derived factorization gives the norm identity and polynomial action
formula recorded in the already existing unfinished L676. Preserve that
canonical file rather than creating a duplicate. Its proof includes the
uniform anchor-only bound <=sqrt(n), the qualified finite-subspace
minimum norm and the exact two-value projection. The rotated variables
above give precisely its formula with H_k=(-1)^k*h_(J-k).

The independent exact script `scripts/one-sided-hankel/inner-factor-polynomial-check.py`
reproduces every n=15 polynomial/inverse coefficient, Schur complement
and norm from the original certificate. It extends the two-value test
to n=27,51. There are exact negative segment points at each tested n;
selected full rational values were inspected. All 21 algebra checks pass,
but the sign constraint fails for these finite candidates. The certificates
contain full coefficients, costs, values and limitations. Finite norm
bounds <=n do not establish a uniform rate or onset.

Full proof and finite enclosures are canonical in
`lemmas/L676-polynomial-angular-inner-inverse-and-normalization.md`.
The exact coordinate construction is useful local progress; this step
is a reproduction/completion of overlapping local work, not a second
discovery or an independent critical audit. Continue the unchanged target
through sign-constrained vectors with a uniform paid cost, retaining all
possible coefficient-zero qualifications. No further finite two-value
fit alone can supply the missing continuum signs.
