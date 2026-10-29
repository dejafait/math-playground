# Signed assembly: inclusive reporting cap failure

Step 484 computes the preliminary exact finite sum without input or
arithmetic failures, but setup and reporting already take 203.597 seconds
at documentation validation, exceeding the authorized inclusive 180-second
cap. No retry is made. Evidence and tentative mathematics remain in L117
and scripts/signed-derivative-assembly/step-484/.

WHY IT FAILS: The cap includes source writing, setup, documentation and
reporting. The script's successful 96.995-second terminal result covers
only the work completed then; it cannot establish the final inclusive
bound. Subsequent proof/checkpoint writing crosses the cap. The preserved
positive interval therefore has no accepted execution-contract claim.
A separately assessed audit may test its mathematical evidence while
retaining this resource failure; it must not silently repair provenance.
