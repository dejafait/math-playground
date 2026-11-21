# Right-ray reproduction working checkpoint1641

Approved target: unchanged SPECIALIZE assessment1640; reproduce its exact
absolute full-theta T_right and A_+ allowance. This is source reproduction,
not a new sign mechanism. Main gap L030-L032/C032a remains independent.

Candidate proof chain, to verify and put in canonical C048g:
C048c gives x0=U/2>3L/8, |V|<pi/2, |w|<L,
v0=pi exp(U)cos V>2r/L^2, |A0|<6r/L and Re A0>0.
The full ray u0+s, s>=0, is in Re u>1 and |Im u|<pi/4.
For upper p, beta=Im p>=0 and y=V/2>=0. Set
Q(x)=(sigma*x+beta*y)/(x^2+y^2), Q(x0)=v0.
For sigma>=0, Q'<=0 since x>y; for sigma<0, Q'<0 while
Q>0 and its decreasing numerator cannot cross back to positive.
Hence Q<=v0 for x>=x0. Integrating the exact phase derivative
gives Re(h(u0+s)-h(u0))<=-v0*(exp(2s)-1-2s).
Reflection covers lower p; real p is included.

K(s)=exp(9s/2)*u0/(u0+s), whose rational factor has modulus<=1.
L799 strip-series identity gives the full theta factor. Its absolute
coefficient sum is <=1+a+20exp(-3t), a<1/14, t=v0 exp(2s)>2.
Since exp(6)>343, this is <1+1/14+20/343<3/2.
The real envelope is (3/2)exp(9s/2-v0*phi(s)). The tangent at
d=1/(3L) has negative slope -lambda, lambda=2v0(exp(2d)-1)-9/2.
Using v0>(19/10)r/L^2 gives lambda>(38/15)r/L^3-9/2
>(62/25)r/L^3, provided r/L^3>675/8. This follows from
monotonicity and exp(12)>160000>145800, via exp(3)>20.
Also v0 phi(d)>(19/45)r/L^4 and 9d/2<=1/8.
Integration thus bounds T_right by
[(3/2)exp(1/8)sqrt(6/pi)/(62/25)] L^(5/2)/sqrt(r)
times exp(-(19/45)r/L^4).
After division by L^(9/2)/r, this is C sqrt(y)exp(-(19/45)y),
y=exp(L)/L^4>=y0. It decreases once y>45/38, satisfied at L=12.

Pending: exact A_+ decimal certificate; full canonical proof with
absolute convergence and normalization; ID-only DAG addition; concise
overview/history/checkpoint; separate conceptual-audit nomination.
Source equation(31), both sigma cases, and AppendixC A_+ were rechecked
only to reproduce the approved target. No extra literature-only step.

Completion: the chain is now canonical in C048g. All 13 exact scalar
comparisons passed; A_+ lies strictly in (0.096513538928204,
0.096513538928205). The separate conceptual audit is nominated in
assessment1641. These saved working notes are not a second canonical proof.
