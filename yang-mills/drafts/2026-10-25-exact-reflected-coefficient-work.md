# Fixed-mesh reflected coefficient: work record

Approved target: extract L003's exact fixed-mesh kappa_a, with both
insertion jets, Wilson and quotient-Haar corrections, and an o_a(g^2)
remainder for Q. Prior coverage is
`literature/2026-10-25-exact-reflected-coefficient-coverage.md`
(SPECIALIZE, supplied at invocation). This is known-method reproduction.

Main gap: interacting continuum Yang–Mills with finite positive
infinite-volume mass, for every compact simple group. Intermediate use:
identify the finite coefficient whose mesh growth/mixing would have to
be controlled before L003's error threshold c_box/2 could be tested.
No uniform estimate, physical coupling trajectory, or continuum axiom
is assumed. Test: complete two-insertion expression and justified
remainder; abandon an expression missing a mean, jet, density term,
or relying on a nonlinear Hodge transfer.

Saved reasoning before full derivation: use H_h=4 sum_(p parallel 12)
h(z_p)P_p, h=theta f,f. Then Q=g^(-4)Cov(H_thetaf,H_f).
On the forest slice set U=exp(gx), and H_h/g^2=h_0+g h_1+g^2 h_2+... .
The rescaled Gaussian density has W_1=-S_3 and
W_2=S_3^2/2-S_4-M_2, with M_2=sum_remaining |x_e|^2/12.
Expand each mean and the joint moment before centering. Odd terms
vanish by x -> -x, not by assuming each cubic jet vanishes.
Only the leading covariance is transferred to L003's Hodge law.

Duplicate/failure check: full L003 and L011 and relevant L004 material
read; the ultraviolet-normalization draft and ATTEMPTS/046 preserve
the scalar-only and direct uniform-source-import failures. L011 is a
method input, not an identification of Gamma with kappa. Its density
and cumulant calculation is reusable; no general Laplace reproof is
needed. Existing notebook changes were inspected and preserved.

Completed the extraction in canonical
[L279](../lemmas/L279-fixed-mesh-exact-reflected-coefficient.md), with the
moving means displayed and a degree-six uncentered joint-moment
remainder before division by g^4. The independent generic cumulant
check agrees exactly (47/80 on both sides), with full evidence in
`../scripts/exact-reflected-coefficient/cumulant-certificate.json`.
No box coefficient was evaluated and no mesh bound follows. Separate
critical review is registered for later approval; this scratch record
is not a second proof location.
