# L989 independent audit working note — step258

Approved target: review256, separately approved in step257. This is
one REPRODUCTION proof audit, using the ready source contracts rather
than another literature search. The supplied overview and DAG were
used before reading the detailed proofs. Existing notebook work is
preserved. No cross-notebook input or mathematical script is used.

Main gap: actual-Xi positivity and actual signed arithmetic payment.
Intermediate target: certify only L989(1)-(10), with the full cutoff
and jump costs strictly below exp(n/2)*n^(-3/2). This could isolate a
technical component before a separate signed mechanism is tested.
Continue if every identity, hypothesis and error passes; repair or
park the first failed term. Success does not pay either signed prefix
or L988's low-zero remainder.

Replay so far: the source at s=1 gives A-J=u-gamma_E-G+V+r,
so G=u-gamma_E+V-A+J+r. The upper-minus-lower convention gives
both signs in (1)-(2). DLMF's normalized factor is n(n+1)/2;
the retained constant correction yields (7), since the difference
after multiplication by 2(n-1) is (n-2)(3n+1). This includes n=2.
The distinct power-of-two candidate gives x'>=x/2 in all cases,
without a lower separation. At u=n,2n the source error multipliers
are at most 9 and 81/4. Multiplication yields exactly the four
terms of (3); each full half-jump gives the corresponding term
of (4). Their ratio to the benchmark is O(n^(9/2)*exp(-n/2)),
which tends to zero. No failure found; canonical audit write-up pending.

Recovery requires a different next action. Compare at most three
independently testable mechanisms, preserve prior signed-payment and
criterion-only stops, and nominate uncovered work as REVIEW_REQUIRED.
No new mathematical claim for that continuation is approved here.

Completion: canonical L989 now contains the accepted independent
audit of (1)-(10), without correction. This supersedes the pending
write-up status above. The different continuation is the exact
endpoint-null three-degree filter in review258, REVIEW_REQUIRED;
no result for that nomination was derived. PROGRESS.md records
the completed audit and the single next source action.
