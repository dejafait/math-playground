# Primitive five-adic scalar domain — bounded specialization

2026-10-08. Approved target and unchanged prior assessment: drafts/literature/2026-10-08-primitive-five-adic-j-domain.md. This is a RESEARCH / REPRODUCTION attempt using foundation 17, with L032's two identities and L035's definition of common scalar witnesses as context. No image computation is attempted.

Work saved before full proof: write t=j/1728 and q=1-t. Since 1728 is a 5-adic unit, the desired domain should consist of (i) integral t with v5(t) a nonnegative multiple of three and v5(q) a nonnegative multiple of four, and (ii) nonintegral t with v5(t) a negative multiple of eleven. Nonintegral t has v5(q)=v5(t). Necessity must show that a primitive witness has either c a unit or a,b units and c a nonunit.

Proposed shared-coordinate sufficiency: choose gamma=0 in case (i), gamma=-v5(t)/11 in case (ii); define alpha=(v5(t)+11 gamma)/3 and beta=(v5(q)+11 gamma)/4. Put b=5^beta. The unit q0=5^(-v5(q))q has an eleventh root u of q0^(-1); set c=5^gamma u. Then q c^11=b^4 exactly. The unit t0=5^(-v5(t))t times u^11 has a cube root w; set a=5^alpha w. This retains the prescribed t and the same c. Cube/eleventh unit-root existence is an application of the cited Hensel theorem, using bijectivity of these powers on F5^* and a unit derivative. It still needs a full necessity/sufficiency proof before being a result.

Discriminating test: reject a domain if any primitive valuation case is omitted, a displayed exponent is not an integer, or the construction supplies separate c values or changes j. A successful domain is only an input to a future comparison of I_pow and I_fiber; neither strictness nor any global twist exclusion follows.

Completed: necessity, simultaneous sufficiency and the disjoint scalar-domain translation are proved in L036. The draft above is retained as the pre-proof checkpoint; full reasoning and source qualifications are canonical in lemmas/L036-primitive-five-adic-common-j-domain.md. No failed valuation case or additional residue restriction was found. The next image-comparison target requires its own approval and must account for classes occurring at multiple scalars.
