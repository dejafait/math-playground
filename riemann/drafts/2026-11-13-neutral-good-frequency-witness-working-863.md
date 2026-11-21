# Fixed neutral good-frequency witness — working863

Approved target: test L750's fixed smooth witness at T=4log3 against
the complete-symbol strict screen c_E>M/(M+1), exactly as assessment861.
This is RESEARCH/REPRODUCTION, not a new observation theorem.

Main gap: actual-Xi all-degree mixed positivity (L030-L032/C032a).
Intermediate target: a certified rejecting witness for the coarse screen.
Use: decide whether that sufficient payment mechanism merits further work.
Continue this test only if exact neutrality, positive norm and certified bad
mass give U=1-b/N_upper <= m0/(1+m0), 0<m0<=-w(0)<=M. Otherwise end
this fixed test as inconclusive; no witness/window/threshold optimization.

Inputs read: L744(6)-(8), L750 Proof1/3 and its interval implementation.
Assessment861 reuses primary quadrature/special-function coverage. The old
T=8log3 numbers are not inputs. Scoped stops L752/C998z/C998 remain as
compared in review860/861. No RH, complement positivity, prime tail or Xi
realization is assumed. Full matching Mathlib coverage not checked.

Exact reasoning to retain: chi is symmetric, supported on [T/40,39T/40]
and one on [T/20,19T/20]. Both odd sine modes are symmetric. Let
a=M_+(phi3)/M_+(phi1) with positive denominator. Then M_+(f)=0
identically and reflection gives M_-(f)=exp(-T/2)M_+(f)=0.
Sine independence on the plateau makes f nonzero for any a.

Planned certificate: reuse only the existing outward elementary interval
implementation in certificate-315.cpp, with its old main renamed. Integrate
real spatial boxes to enclose the exact moments and norm, and centered real
Fourier integrals on rational frequency boxes. Include all prime powers below
81, recurrence and sector-remainder errors. Save every retained box, Fourier
bound and scalar value, plus failure flags. Spatial Plancherel is total mass;
unselected frequencies contribute no assumed sign and no discarded tail.

Unfinished at initial save: coefficient/norm enclosures, w(0), actual bad boxes,
bad mass, the required comparison and implementation checks.

Completed 14 November2026: the fixed test certifies rejection; full proof is
C750a and full evidence is `scripts/good-frequency/fixed-witness-863.json`.
The rational subset J=[-1/2,1/2] union +/-[45/32,47/32] has bad mass
>0.10416, while N<2.63863 and w(0)<-36.06981. Thus c_E<=317/330<36/37
<=M/(M+1). All31 prime-power records, all18 reflected-pair box records and
the exact-ratio/norm/scalar bounds were inspected in full. No omitted
frequency mass is priced. This is a negative screen result, not Q<0 or RH.
No witness/length/threshold tuning was performed. Only nominal dyadic output
endpoints were corrected after the first successful certificate to distinguish
integration intervals from inflated evaluation boxes; computed bounds agree.
The failed JSON root-pointer inspection made no mathematical claim; all
load-bearing selected fields were then inspected directly in full.

Remaining verification is a separate conceptual audit, nominated in
`drafts/literature/2026-11-14-fixed-neutral-screen-rejection-audit-863.md`.
No claim of progress beyond assessed sources or an independently checked
arithmetic implementation is made. PROOF's main assembly is unchanged.
