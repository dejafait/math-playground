# Suzuki full decomposition audit1124 — working record

Approved scope: assessment1123, full three-term identity and existential
small-window coercivity for arbitrary complex L2 tests. C618a is the
sole local mathematical input. No all-support signing is attempted.

Working argument, not yet a completed canonical result: extend each
source component g_j on t>=0 by zero to t<0, multiply by exp(-ct),
and apply L1 Fourier inversion to its transform B_j(r+ic)/(r+ic)^2.
The transforms are absolutely integrable; the one-sided functions
are continuous at zero and vanish there. Inversion gives both spatial
signs directly, including the zero value of the inverse at negative
arguments, without an informal c-to-infinity limit. Combine the two
signs and form the increment kernel before shifting the gamma contour.
Its two quotient factors remove z=0, and its vertical edges should be
O(log(R)/R^2) uniformly on the compact spatial square. Check all bounds
and the normalization against the primary PDF before promoting this.

Candidate bookkeeping to check: on Re(s)=1/2+c choose a common bound M
for P and Z. Four shifted products give |I0+I1|<=4 M C2 E0/(2pi).
With W the actual half-digamma weight, W>=C outside [-T,T] and W>=-D
inside, Iinfinity>=2[C E0-(C+D)L_T]/(2pi). Thus the candidate
coefficient is 2[C-2 M C2-(C+D)a C3]/(2pi). C618a supplies C2 and
C3. Strict positivity also needs E0 injectivity from its primitive.
No numeric onset, Mathlib formalization or RH implication is claimed.

Completed: the proof and all load-bearing estimates are now canonical
in C618b. The candidate coefficient above was verified with
C=2 M C2+1 and a0=min(a1,1/[2(C+D)C3]), giving Q>=E0/(2pi).
One-sided L1 inversion handles both spatial signs; the gamma contour
is shifted only after the increment quotients remove zero. The full
complex-test Fubini bound and E0 injectivity are explicit in C618b.
This working record is retained as the unfinished-reasoning checkpoint,
not a second proof or a current task record. Independent review remains
the sole next action recorded in PROGRESS.md.

Preservation: pre-existing notebook changes remain untouched. The first
scoped git status was excessively verbose and truncated; it was not
used as evidence. Relevant source comparison and C618a were read in
full, and distinct parameter/square-order stops were inspected narrowly.
