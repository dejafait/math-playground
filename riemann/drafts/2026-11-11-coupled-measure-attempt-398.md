# Working checkpoint for the approved coupled-range test — step398

Target: the unchanged representing-measure target approved in review396.
Main gap: actual-Xi positivity/forcing and the selected complete-kernel
bridge remain open. A small exact representing norm would combine with
C997y's cap gap, while an actual-span witness can disprove that norm
target without deciding the capped residual objective.

Preserved partial reasoning, before further estimates: test the band-only
spectral polynomial h_n(t)=exp(2it) sin((t-2n)/(8n))^n. Its binomial
expansion uses exactly gamma_j=15/8+j/(4n); hence its complete response
is in the actual coupled span, including the same lower window.
The two windows place this sine near zero, whereas its centered
order-ceil(sqrt(n)) derivative at t=0 may retain exponential size.
Needed: a rigorous noncancellation bound for that derivative, an upper
bound on the COMPLETE response on I, and their rate comparison.
No conclusion is claimed at this checkpoint. No coefficient cap is
imposed on a test vector in the linear span; it must not be mistaken
for an admissible target-minus-capped-band residual.

Inputs read: C997c's real-t complete-kernel variation bound, C997s's
kernel/grid/objective, C997t(6)'s coupled endpoints, C997y(8)-(13) and
its step395 audit. Review395 and stops340/341/393/396 are reused.
The query for sine/binomial band-column constructions found C997f's
positive-binomial measure construction and C997w's Hermite construction
as comparisons to inspect narrowly; neither is assumed to be new here.
Stop this candidate if its centered derivative cannot be bounded without
an unpaid cancellation assumption. The approved rate is 1/64, with a
strict saving required for an upper bound; no finite sample proves it.

Completed in step398: the candidate was resolved by a finite Leibniz
partition bound, with every nonsingleton term paid. The full result and
proof are canonical in C997z, not in this preserved working checkpoint.
It gives a lower exponential norm rate greater than 7/16 on the actual
band span; the original exact representing-norm target is false, subject
to independent audit. C997f and C997w were narrowly checked and use
different objects. No approximate-measure or capped-E_n inference was
made. The preceding tentative notes are retained as unfinished-work
history, not as active instructions.
