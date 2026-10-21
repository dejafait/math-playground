# Local invariant degree specialization — step 276 working checkpoint

Approved target: Assess finiteness and generic degree at most two for the local coarse classifying germ of L101/L102 via full-group invariants.
Prior ready coverage: literature/2026-10-14-split-line-local-classifying-degree.md (SPECIALIZE).
Inputs read: audited L094, L101, L102; scoped ATTEMPTS/046,/061 and histories/261,/265,/274. No duplicate local degree proof found; their global/quadratic/curvature stops remain.

Main gap: universal primitive rational Hodge realization. Local target could control parameter identification near the split bundle; it supplies no common F, quaternionic integration or transport.

Working argument, pending complete write-up: take H=H_+ plus H_- with full effective ratio-C* weights +1,-1. Its polynomial invariants are all p_i q_j. On the actual alpha(s,t), choose bases with p_1=s+O(2), p_2=-t+O(2), q_1=t+O(2), q_2=s+O(2). Both coordinate pairs generate m=(s,t) in B=C{s,t}, by the analytic inverse-function theorem. Thus the ideal of all products is exactly m^2, without discarding higher coefficients. This isolates the central fibre. Imported finite-germ/image criteria supply finite inclusion A=O_(reduced analytic image,0) into B, with dim A=2. B/m_A B=B/m^2 has length 3, so Nakayama bounds generic rank d by 3. The imported finite-extension formula gives d e_A(m_A)=e_B(m^2)=4. Since e_A is a positive integer, d divides 4, hence d is 1 or 2. Need document all ring/local/residue-field hypotheses and reduced analytic quotient scope. Do not infer a literal involution, exact degree two or one, quaternionic structure or arbitrary algebraic/weakly-normal coarse-germ identification.

Continuation/abandonment test: finish exact invariant-ring and local-ideal verification for the complete convergent alpha; stop if the actual analytic quotient or finiteness hypotheses fail. Achieved proposed bound is at most two, required at most two. No scripts or numerical evidence are needed. Save full proof as L103 only after checking these passages; independent critical review remains a future action.

Completed: full proof and source qualifications are canonical in L103; generic degree is one or two for the reduced analytic GIT image. Recorded as ADVANCE / REPRODUCTION pending separate critical audit, with no quaternionic or global conclusion. No mathematical script was needed.
