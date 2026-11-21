# Finite weighted Landau formula: inspected source input

Source review254, 10 November2026. This records an existing theorem,
not a new endpoint estimate or a specialization proved in this turn.

## Hypotheses

O. Gorodetsky, *Smooth numbers and the Dickman rho function*,
[arXiv2211.08973v6, 19December2023](https://arxiv.org/pdf/2211.08973v6#page=15),
Section5.2, Lemma5.2, printed p15, equations(5.5)-(5.6).
Its proof is AppendixA, printed pp21-22. The
[HTML rendering](https://arxiv.org/html/2211.08973v6#S5.SS2)
renumbers the same displayed statement as(5.10)-(5.11); use the
PDF numbering in citations. The source's conventions on printed p3
make the unadorned implied constants absolute.

Let x>=4 be real, T>=2+|Im(s)|, and let s be a complex parameter
at which zeta is nonzero. The source explicitly includes s=1 with
the replacement below. For the displayed general formula avoid
the other singular parameters s=-2k, k>=1. Only s=1 is intended
for subsequent notebook use; no continuation at a trivial zero is
imported here.

Define

    S_1(x,s)=sum'_(m<=x) Lambda(m)*m^(-s),

where Lambda is the actual von Mangoldt function and the prime
on the sum assigns half the last term when x is a prime power.
Let x' be a nearest prime power to x other than x itself, and put
<x>=|x-x'|. The summation over nontrivial zeros has analytic
multiplicity. No RH or simple-zero assumption is made.

## Conclusion

The cited source states

    S_1(x,s)=x^(1-s)/(1-s)-zeta'(s)/zeta(s)
      -sum_(|Im(rho-s)|<=T) x^(rho-s)/(rho-s)
      +sum_(k>=1) x^(-2*k-s)/(2*k+s)+R_1(x,T,s),

    |R_1(x,T,s)| << (log x)*(x')^(-Re(s))
                              *min{1,x/(T*<x>)}
       +[log^2(x*T)/T]
                      *[2^|Re(s)|*x^(1-Re(s))+2^(-Re(s))/log x].

At s=1, the source explicitly replaces the combined first two
terms by log x-gamma_E, where gamma_E is Euler's constant.
The cutoff includes equality; it is not a choice of a good-height
subsequence. Both arithmetic prime powers and trivial zeros are
retained. A full last arithmetic term instead of a midpoint term
requires its half-jump to be restored, as prescribed by the source's
definition. No bound for that later endpoint-weighted correction
has been derived here.

## Proof

Import Lemma5.2 by the above precise citation, without reproof.
The complete relevant AppendixA cases were inspected. Perron
starts with a_n=Lambda(n)n^(-s) and
sigma_0=max{0,1-Re(s)}+1/log x. The near arithmetic term is
separated from the remaining terms in x/2<m<2x, m!=x.
The contour uses two heights in[T,T+1], then returns the zero
sum to the stated closed interval at T. Its incurred bound is
x^(1-Re(s))*log(T)/T. Residues give the analytic orders of zeros;
the double pole when s=1 has the explicitly stated residue.
The proof bounds the middle, right and left horizontal pieces
separately, and the far left vertical piece vanishes as its
abscissa tends to minus infinity. Thus the printed theorem needs
neither clearance from a zero ordinate nor an arithmetic endpoint.

For the proposed s=1 use, all nontrivial-zero denominators are
nonzero and the trivial-zero series converges absolutely. This
does not license differentiating the finite-height error in s,
passing a conditional zero sum to infinite height, identifying
the sum with B_n, or inferring a sign for S_1(x,1)-log x+gamma_E.
The source prints -(zeta/zeta)' at one point in the Perron error
discussion; the surrounding integrand and statements use
-zeta'/zeta. That typographical expression is not imported as
an identity.

Supporting source checked: H.L. Montgomery and R.C. Vaughan,
*Multiplicative Number Theory I: Classical Theory*, Cambridge,
2007, [Chapter12, pp397-401](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf),
Lemmas12.1,12.2,12.4 and Theorem12.5/(12.3)-(12.4), including
the Perron near/far split and contour proof. This is supporting
coverage for the source's method; its denominator rho is not
silently substituted for rho-1. The named Perron inputs remain
standard cited inputs, not an independently reconstructed book.

## Mathlib

Full matching Mathlib coverage is unchecked and unknown. No
absence claim or formal verification is made. Lemma5.2 is a
literature input; its notebook-specific endpoint specialization
and complete error comparison remain future work.
