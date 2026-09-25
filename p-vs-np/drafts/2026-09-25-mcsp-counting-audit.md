# Archived MCSP counting audit sketch — 2026-09-25

The shared rules, local goal, checkpoint, whole proof overview and DAG, existing changes, earlier attempt notes, and the preceding completeness assessment were read. None of the earlier lemmas tests circuit counting for the MCSP decision predicate. The current Clay page and Cook's linked official description were rechecked; the existing source date remains accurate. Existing work is preserved.

**Gap and intermediate target.** MCSP has direct NP certificates, but a circuit-size lower bound for a function represented by a table is not yet a lower bound for deciding whether that table has a small circuit. Write r for the represented function's number of variables, N=2^r for its table length, and M for the full MCSP input length, including a unary gate threshold s. The target is a quantitative counting-versus-recognition test. A valid transfer to superpolynomial decision complexity in M would supply a separation route. An unbounded threshold range with polynomial-time exact recognition and almost universal rejection would reject density alone as that transfer. Even after a useful counting fact, uniform explicitness and unrestricted decision hardness would remain unresolved.

**Saved derivation.** Use the existing AND/OR/NOT basis with no free constants, and allow an input wire as output. Encode the instance as 1^r 0 T 1^s, where |T|=2^r and r>=1; M=N+r+1+s. Topologically ordered descriptions of at most s gates number at most

B(r,s)=(s+1)(r+s)[3(r+s)^2]^s.

Thus at most B(r,s) tables are YES instances. For r>=8 and s=floor(N/(32r)), log_2 B <= 2r+s(2+2r) <= N/4. At least 1-2^(-3N/4) of all tables therefore have circuit size exceeding s. This is only Omega(N/log N) for the represented function. A direct DNF construction has at most 2rN gates for every table.

Put ell=ceil(log_2(r+2)) and b(r)=floor(r/(16 ell)). If s<=b(r), then log_2 B <= 2ell+1+r/4 <= 3r for r>=2, hence B<=N^3; r=1 is direct. Enumerating those descriptions and checking each on all N assignments is an exact polynomial-time decider on this unbounded threshold range. The YES fraction is at most N^3/2^N. This is the proposed discriminator against density-to-hardness, not a polynomial-time decider for all thresholds.

**Completion.** [L006](../lemmas/L006-mcsp-counting-versus-decision.md) completes the derivation and reviews unary parsing, NOT descriptions, output-wire choices, constants via ordinary gates, integer rounding, small r, and uniform enumeration. The exact low-threshold algorithm supplies the preselected discriminator against rejection density alone. The saved finite-check script tests only constants and rounding. General MCSP_u recognition and P versus NP remain unresolved; this archive carries no unfinished proof or current action.
