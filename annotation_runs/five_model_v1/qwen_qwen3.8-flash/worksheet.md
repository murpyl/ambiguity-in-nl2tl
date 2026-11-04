# Model-generated annotation worksheet
Model: qwen/qwen3.8-flash
Times below are actual orchestration timestamps (UTC).
Stage 1 started: 2026-11-04T00:49:28.185211+00:00; completed: 2026-11-04T00:54:03.853201+00:00
Stage 2 started: 2026-11-04T00:54:03.855204+00:00; completed: 2026-11-04T01:01:07.363435+00:00

## Stage 1 (frozen)

### R001 / item_0001 (joint_separate)
A pulse and a flash must eventually occur.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R001", "comments": "Open interpretation only.", "interpretations": ["At some step in the future, a pulse occurs and at some step a flash occurs; order and simultaneity are unrestricted.", "There exists a finite time by which both a pulse and a flash have occurred, possibly on different steps."]}

### R002 / item_0002 (joint_separate)
Pulses and flashes must keep occurring.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R002", "comments": "Open interpretation only.", "interpretations": ["Pulses occur infinitely often and flashes occur infinitely often.", "From some point onward, the system keeps producing pulses and flashes repeatedly, without necessarily requiring a fixed pattern."]}

### R003 / item_0003 (joint_separate)
Every request must be followed by a pulse and a flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a request occurs"}
{"review_id": "R003", "comments": "Open interpretation only.", "interpretations": ["For every request, a pulse and a flash must occur at some later step or steps; their order is not fixed.", "For every request, both a pulse and a flash are required after it, possibly including the same step as the request."]}

### R004 / item_0004 (joint_separate)
A pulse and a flash must occur before any stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R004", "comments": "Open interpretation only.", "interpretations": ["If a stop occurs, then before that stop there must have been at least one pulse and at least one flash.", "No stop may occur until both a pulse and a flash have occurred."]}

### R005 / item_0005 (joint_separate)
After each request, a pulse and a flash are required before the next stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a request occurs", "d": "a stop occurs"}
{"review_id": "R005", "comments": "Open interpretation only.", "interpretations": ["For every request, before the next stop after that request, both a pulse and a flash must occur.", "If there is no next stop, the pulse and flash are still required eventually, because the request creates an obligation."]}

### R006 / item_0006 (joint_separate)
The signal and the indicator must eventually be active for two consecutive steps.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R006", "comments": "Open interpretation only.", "interpretations": ["There is some step t such that the signal and the indicator are both active at t and at t plus one.", "Both the signal and the indicator must be simultaneously active for a continuous run of at least two steps at some point."]}

### R007 / item_0007 (joint_separate)
The signal and the indicator must eventually become active.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R007", "comments": "Open interpretation only.", "interpretations": ["The signal becomes active at some future step and the indicator becomes active at some future step, not necessarily the same step.", "Both the signal and the indicator must eventually be active, without any requirement that they remain active."]}

### R008 / item_0008 (joint_separate)
Eventually the signal and the indicator must be active until a release occurs.
{"a": "a signal is active", "b": "an indicator is active", "c": "a release occurs"}
{"review_id": "R008", "comments": "Open interpretation only.", "interpretations": ["From some step onward, the signal and the indicator are active and remain active until a release occurs.", "If no release occurs, then from that eventual point the signal and the indicator remain active forever."]}

### R009 / item_0009 (joint_separate)
A pulse and a flash must occur with a completion afterward.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a completion occurs"}
{"review_id": "R009", "comments": "Open interpretation only.", "interpretations": ["There exists a pulse and a flash that occur before some completion event.", "A pulse and a flash must occur at some point, and a completion must occur later than them."]}

### R010 / item_0010 (joint_separate)
After a start, a pulse and a flash must occur before a finish.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a start occurs", "d": "a finish occurs"}
{"review_id": "R010", "comments": "Open interpretation only.", "interpretations": ["If a start occurs, then before the next finish after that start, both a pulse and a flash must occur.", "If no finish occurs after the start, the pulse and flash are still eventually required by the start."]}

### R011 / item_0011 (joint_separate)
A pulse immediately followed by a flash and a click immediately followed by a mark must eventually occur.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a click occurs", "d": "a mark appears"}
{"review_id": "R011", "comments": "Open interpretation only.", "interpretations": ["There is a step where a pulse occurs and the immediately next step where a flash occurs, and separately there is a step where a click occurs and the immediately next step where a mark appears.", "The pulse-flash pair and the click-mark pair may occur at different times, but each pair must be consecutive."]}

### R012 / item_0012 (joint_separate)
The signal and the indicator must keep being active for two consecutive steps.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R012", "comments": "Open interpretation only.", "interpretations": ["Infinitely often, the signal and the indicator are both active for two consecutive steps.", "The requirement is that active periods of the signal and indicator keep recurring and each such period lasts at least two consecutive steps."]}

### R013 / item_0001 (next_later)
Every pulse must be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R013", "comments": "Open interpretation only.", "interpretations": ["For every pulse, a flash must occur at some strictly later step.", "For every pulse, a flash must occur after it, possibly immediately after, but not necessarily on the same step."]}

### R014 / item_0002 (next_later)
If there is a pulse now, a flash must follow.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R014", "comments": "Open interpretation only.", "interpretations": ["If a pulse occurs at the current step, then a flash must occur at some future step.", "If a pulse occurs now, a flash must occur immediately after, for example at the next step."]}

### R015 / item_0003 (next_later)
There must be at least one pulse followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R015", "comments": "Open interpretation only.", "interpretations": ["There exists at least one pulse followed later by at least one flash.", "At least one pulse-flash sequence occurs, while other pulses may be unconstrained."]}

### R016 / item_0004 (next_later)
After every pulse, the indicator must then stay on permanently.
{"a": "a pulse occurs", "b": "the indicator is on"}
{"review_id": "R016", "comments": "Open interpretation only.", "interpretations": ["For every pulse, after that pulse the indicator becomes on and remains on forever.", "For every pulse, the indicator must be on from the pulse step or the next step onward and never turn off."]}

### R017 / item_0005 (next_later)
A stop must occur, and before the first stop every pulse must be followed by a flash, even if that flash comes after the stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R017", "comments": "Open interpretation only.", "interpretations": ["At least one stop occurs, and every pulse before the first stop must have some later flash, even if that flash occurs after the stop.", "The obligation applies only to pulses in the prefix before the first stop, but their flash fulfillment is not limited to that prefix."]}

### R018 / item_0006 (next_later)
Every pulse must be followed by a flash, with a chime at some strictly later step than that flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a chime occurs"}
{"review_id": "R018", "comments": "Open interpretation only.", "interpretations": ["For every pulse, there is a later flash, and after that flash there is a strictly later chime.", "Each pulse must be followed by a flash-chime sequence, with the chime occurring at a step after the flash."]}

### R019 / item_0007 (next_later)
A pulse must never be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R019", "comments": "Open interpretation only.", "interpretations": ["No pulse may have a flash at any strictly later step.", "If a pulse occurs, then a flash must never occur afterward, though a flash before the pulse may be allowed."]}

### R020 / item_0008 (next_later)
Every pulse must be followed by a flash before any subsequent stop, with no stop at the flash step.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R020", "comments": "Open interpretation only.", "interpretations": ["For every pulse, before the next stop after that pulse, a flash must occur, and the flash step must not also be a stop.", "If there is no subsequent stop, the pulse still requires a flash eventually, but the stop-related constraint is vacuous."]}

### R021 / item_0009 (next_later)
Every pair of pulses on consecutive steps must be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R021", "comments": "Open interpretation only.", "interpretations": ["Whenever pulses occur on two consecutive steps, a flash must occur at some later step after that pair.", "The obligation is triggered only by consecutive-pulse patterns, not by isolated pulses."]}

### R022 / item_0010 (next_later)
Eventually, the rule that every pulse is followed by a flash must hold from then on.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R022", "comments": "Open interpretation only.", "interpretations": ["There exists a step N such that every pulse at or after N is followed by a flash at a later step.", "Before N, pulses may be unfulfilled; after N, the pulse-to-flash rule holds permanently."]}

### R023 / item_0011 (next_later)
A pulse followed by a flash must occur over and over without end.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R023", "comments": "Open interpretation only.", "interpretations": ["Infinitely often, a pulse occurs and is followed later by a flash.", "The pulse-flash sequence must repeat without end, though the spacing between occurrences is not fixed."]}

### R024 / item_0012 (next_later)
Once an activation occurs, every pulse from that step onward must be followed by a flash.
{"a": "an activation occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R024", "comments": "Open interpretation only.", "interpretations": ["At the first activation step, every pulse from that step onward must be followed by a flash at a later step.", "Pulses before activation are unconstrained, but activation starts a permanent pulse-to-flash obligation."]}

### R025 / item_0001 (same_later)
Requests require an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R025", "comments": "Open interpretation only.", "interpretations": ["Every request must be accompanied or followed by an active response.", "Every request requires an active response, possibly at the same step or at a later step."]}

### R026 / item_0002 (same_later)
A request at the starting step requires an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R026", "comments": "Open interpretation only.", "interpretations": ["If a request occurs at the initial step, then an active response must occur at some later step.", "If a request occurs at the initial step, then an active response must occur immediately, possibly at the same or next step."]}

### R027 / item_0003 (same_later)
There must be a request with an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R027", "comments": "Open interpretation only.", "interpretations": ["There exists at least one step where a request occurs and the response is active at that step.", "There exists at least one request that is followed by an active response."]}

### R028 / item_0004 (same_later)
Requests with an active response must keep occurring.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R028", "comments": "Open interpretation only.", "interpretations": ["Infinitely often, a request occurs together with an active response.", "The pattern of request with active response must keep recurring without end."]}

### R029 / item_0005 (same_later)
Eventually, requests must always have an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R029", "comments": "Open interpretation only.", "interpretations": ["There exists a step N such that from N onward, every request has an active response.", "Eventually, no request may occur without an active response."]}

### R030 / item_0006 (same_later)
Requests require an active response until a release occurs, and a release must occur.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R030", "comments": "Open interpretation only.", "interpretations": ["A release must occur, and before that release every request requires an active response.", "After the release, requests no longer require an active response."]}

### R031 / item_0007 (same_later)
Requests require an active response unless and until a release occurs.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R031", "comments": "Open interpretation only.", "interpretations": ["If no release occurs, then every request forever requires an active response.", "Once a release occurs, the request-response requirement ends; release is optional."]}

### R032 / item_0008 (same_later)
From the first release onward, requests require an active response.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R032", "comments": "Open interpretation only.", "interpretations": ["Starting at the first release step, every later request requires an active response.", "Requests before the first release are unconstrained, but requests at or after the first release are obligated."]}

### R033 / item_0009 (same_later)
Every request requires a response that remains active forever.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R033", "comments": "Open interpretation only.", "interpretations": ["For every request, the response becomes active at some point and then remains active forever.", "Each request triggers a permanent active response, possibly starting at the request step or later."]}

### R034 / item_0010 (same_later)
Every request requires the response to stay active until a release, which must occur.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R034", "comments": "Open interpretation only.", "interpretations": ["For every request, the response must remain active until a later release, and at least one release must occur.", "Each request creates a continuous active-response obligation ending at a mandatory release."]}

### R035 / item_0011 (same_later)
A request at the next step requires an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R035", "comments": "Open interpretation only.", "interpretations": ["If a request occurs at the next step, then an active response must occur at some later step.", "If a request occurs at the next step, then an active response must occur immediately, possibly at that next step or the step after it."]}

### R036 / item_0012 (same_later)
Requests made while the response is permitted require an active response.
{"a": "a request occurs", "b": "the response is active", "c": "the response is permitted"}
{"review_id": "R036", "comments": "Open interpretation only.", "interpretations": ["Any request that occurs while the response is permitted must have an active response later.", "Only requests made during permitted states create an active-response obligation; other requests are unconstrained."]}

### R037 / item_0001 (trigger_scope_final)
A pulse is to be followed by a flash, possibly at the same step.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R037", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, a flash must occur at the same step or at a later step.", "There exists a pulse that is followed by a flash, possibly on the same step."]}

### R038 / item_0002 (trigger_scope_final)
A pulse requires the light to be on at that step.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R038", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, the light must be on at that same step.", "At least one pulse must coincide with the light being on."]}

### R039 / item_0003 (trigger_scope_final)
A pulse is to have a flash at the next step.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R039", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, a flash must occur exactly at the next step.", "There exists a pulse followed immediately by a flash on the next step."]}

### R040 / item_0004 (trigger_scope_final)
A pulse requires the light to stay on from that step onward.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R040", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, the light must be on from that step onward and remain on forever.", "A pulse triggers permanent light-on beginning at the pulse step."]}

### R041 / item_0005 (trigger_scope_final)
A pulse calls for the light to be on until a release occurs, with a release required.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R041", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, the light must be on until a release occurs, and a release is required.", "A pulse creates a light-on obligation that ends only at a mandatory later release."]}

### R042 / item_0006 (trigger_scope_final)
A pulse calls for the light to stay on until a release, or forever if no release comes.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R042", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, the light must stay on until a release; if no release occurs, the light stays on forever.", "A pulse creates a liveness obligation for the light to remain on through the first subsequent release, if any."]}

### R043 / item_0007 (trigger_scope_final)
A pulse calls for the light to be on at the first release at or after that pulse, and that release must occur.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R043", "comments": "Open interpretation only.", "interpretations": ["For every pulse, there must be a first release at or after that pulse, and at that release step the light must be on.", "The pulse does not require the light to stay on continuously, only to be on at the first relevant release."]}

### R044 / item_0008 (trigger_scope_final)
A pulse calls for a release before any flash from that step onward, and a flash at or after the release.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a release occurs"}
{"review_id": "R044", "comments": "Open interpretation only.", "interpretations": ["For every pulse, before any flash at or after that pulse, a release must occur; then a flash must occur at or after that release.", "The required order is pulse, then release, then flash, with no flash before the release."]}

### R045 / item_0009 (trigger_scope_final)
A pulse while enabled calls for a flash at that step or later.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "an enable state holds"}
{"review_id": "R045", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs while the enable state holds, a flash must occur at that step or later.", "Only enabled pulses create a flash obligation; pulses while disabled are unconstrained."]}

### R046 / item_0010 (trigger_scope_final)
Before the first stop, a pulse calls for a flash at that step or later.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R046", "comments": "Open interpretation only.", "interpretations": ["For any pulse occurring before the first stop, a flash must occur at the pulse step or later.", "The flash obligation is triggered by pre-stop pulses, but the flash itself is not explicitly restricted to occur before the stop."]}

### R047 / item_0001 (negation_scope)
The first and second indicators must not be active now.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R047", "comments": "Open interpretation only.", "interpretations": ["At the current step, neither the first indicator nor the second indicator is active.", "Both indicators must be inactive now, with no constraint on later steps."]}

### R048 / item_0002 (negation_scope)
The first and second indicators must never be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R048", "comments": "Open interpretation only.", "interpretations": ["At every step, neither the first indicator nor the second indicator is active.", "Both indicators must remain inactive forever."]}

### R049 / item_0003 (negation_scope)
At some point, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R049", "comments": "Open interpretation only.", "interpretations": ["There exists at least one step where neither the first indicator nor the second indicator is active.", "At some future time, both indicators must be inactive simultaneously."]}

### R050 / item_0004 (negation_scope)
Infinitely often, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R050", "comments": "Open interpretation only.", "interpretations": ["There are infinitely many steps where neither the first indicator nor the second indicator is active.", "The state in which both indicators are inactive must recur forever."]}

### R051 / item_0005 (negation_scope)
From some point onward, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R051", "comments": "Open interpretation only.", "interpretations": ["There exists a step N such that from N onward, neither indicator is active.", "Eventually, both indicators become permanently inactive."]}

### R052 / item_0006 (negation_scope)
The first and second indicators must not be active until a release occurs, and a release must occur.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a release occurs"}
{"review_id": "R052", "comments": "Open interpretation only.", "interpretations": ["A release must occur, and before that release neither indicator may be active.", "After the release, the indicators may become active."]}

### R053 / item_0007 (negation_scope)
The first and second indicators must not be active until a release occurs; release is optional.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a release occurs"}
{"review_id": "R053", "comments": "Open interpretation only.", "interpretations": ["Neither indicator may be active until a release occurs; if no release occurs, they remain inactive forever.", "If a release occurs, the inactivity requirement holds up to that release, and release is optional."]}

### R054 / item_0008 (negation_scope)
Whenever the gate is open, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "the gate is open"}
{"review_id": "R054", "comments": "Open interpretation only.", "interpretations": ["At every step where the gate is open, neither indicator is active.", "The open gate forbids active indicators at the same step."]}

### R055 / item_0009 (negation_scope)
Whenever a pulse occurs, the first and second indicators must not be active at the immediately following step.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs"}
{"review_id": "R055", "comments": "Open interpretation only.", "interpretations": ["For every pulse at step t, neither indicator is active at step t plus one.", "Each pulse triggers a one-step inactive period for both indicators immediately afterward."]}

### R056 / item_0010 (negation_scope)
Whenever a pulse occurs, there must be a step at that time or later when the first and second indicators are not active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs"}
{"review_id": "R056", "comments": "Open interpretation only.", "interpretations": ["For every pulse at step t, there exists some step t prime greater than or equal to t where neither indicator is active.", "The inactive step may be the pulse step itself or any later step."]}

### R057 / item_0011 (negation_scope)
Whenever a pulse occurs, the first and second indicators must not be active until a release occurs at that step or later, and such a release is required.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs", "d": "a release occurs"}
{"review_id": "R057", "comments": "Open interpretation only.", "interpretations": ["For every pulse at step t, a release must occur at some step t prime greater than or equal to t, and neither indicator may be active until that release.", "Each pulse creates a mandatory release and an inactivity period lasting until that release."]}

### R058 / item_0012 (negation_scope)
A check must occur at a step when the first and second indicators are not active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a check occurs"}
{"review_id": "R058", "comments": "Open interpretation only.", "interpretations": ["There exists a step where a check occurs and neither indicator is active.", "At least one check must coincide with both indicators being inactive."]}

### R059 / item_0001 (or_scope)
Requests are answered by a pulse or a flash.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R059", "comments": "Open interpretation only.", "interpretations": ["Every request must be followed by at least one of a pulse or a flash.", "A request may be answered by a pulse, by a flash, or by both, but at least one must occur."]}

### R060 / item_0002 (or_scope)
After a request, the next step must contain a pulse or a flash.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R060", "comments": "Open interpretation only.", "interpretations": ["For every request at step t, either a pulse or a flash occurs at step t plus one.", "The response must occur exactly on the next step, not merely later."]}

### R061 / item_0003 (or_scope)
A request must be answered at once by a pulse or a flash, but not both.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R061", "comments": "Open interpretation only.", "interpretations": ["For every request, a pulse or a flash must occur immediately, possibly at the same step, and exactly one of them must occur.", "For every request, the immediate next step must contain either a pulse or a flash, but not both."]}

### R062 / item_0004 (or_scope)
Every request starts a pulse-then-flash or flash-then-pulse response, with the two events on consecutive steps.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R062", "comments": "Open interpretation only.", "interpretations": ["For every request at step t, either a pulse occurs at t plus one and a flash occurs at t plus two, or a flash occurs at t plus one and a pulse occurs at t plus two.", "Each request starts a two-step response consisting of one pulse and one flash in either order."]}

### R063 / item_0005 (or_scope)
A request requires the first or second signal to stay active until a release, which must eventually occur.
{"a": "a request occurs", "b": "the first signal is active", "c": "the second signal is active", "d": "a release occurs"}
{"review_id": "R063", "comments": "Open interpretation only.", "interpretations": ["For every request, either the first signal or the second signal must remain active until a later release, and a release must eventually occur.", "A request chooses one of the two signals to hold active until a mandatory release ends the obligation."]}

### R064 / item_0006 (or_scope)
A request requires the first or second signal to remain active unless released; release is optional.
{"a": "a request occurs", "b": "the first signal is active", "c": "the second signal is active", "d": "a release occurs"}
{"review_id": "R064", "comments": "Open interpretation only.", "interpretations": ["For every request, either the first signal or the second signal must remain active until a release; if no release occurs, it remains active forever.", "The active-signal obligation ends only if a release occurs, but release is optional."]}

### R065 / item_0007 (or_scope)
Until a stop occurs, requests must receive an immediate pulse or flash; a stop must eventually occur.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R065", "comments": "Open interpretation only.", "interpretations": ["A stop must eventually occur, and before that stop every request must receive an immediate pulse or flash.", "The immediate-response requirement applies until the first stop, and the stop is mandatory."]}

### R066 / item_0008 (or_scope)
Unless a stop occurs, requests must receive an immediate pulse or flash; a stop is not required.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R066", "comments": "Open interpretation only.", "interpretations": ["If no stop occurs, then every request forever requires an immediate pulse or flash.", "If a stop occurs, the immediate-response requirement ends at that stop, but the stop is not required."]}

### R067 / item_0009 (or_scope)
Requests must receive a pulse or flash before the next stop.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R067", "comments": "Open interpretation only.", "interpretations": ["For every request, before the next stop after it, a pulse or a flash must occur.", "If there is no next stop, the pulse or flash is still eventually required by the request."]}

### R068 / item_0001 (until_termination)
The state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R068", "comments": "Open interpretation only.", "interpretations": ["From some relevant point, the state remains active until a release occurs.", "If no release occurs, the state remains active forever."]}

### R069 / item_0002 (until_termination)
Whenever a request occurs, the state must remain active until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a request occurs"}
{"review_id": "R069", "comments": "Open interpretation only.", "interpretations": ["For every request at step t, the state must remain active from t or a later step until a release occurs.", "Each request creates an active-state obligation that ends at a release, possibly requiring eventual release."]}

### R070 / item_0003 (until_termination)
Eventually, the state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R070", "comments": "Open interpretation only.", "interpretations": ["There exists a step N such that from N onward the state remains active until a release occurs.", "Before N the state may be inactive; after N it becomes active and stays active until release."]}

### R071 / item_0004 (until_termination)
From every step onward, the state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R071", "comments": "Open interpretation only.", "interpretations": ["At every step, the state must be active and remain active until a release occurs.", "The obligation to stay active until release holds globally from every step, implying permanent activity if no release occurs."]}

### R072 / item_0005 (until_termination)
The state must remain active and the indicator lit until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "the indicator is lit"}
{"review_id": "R072", "comments": "Open interpretation only.", "interpretations": ["The state remains active and the indicator remains lit until a release occurs.", "If no release occurs, the state remains active and the indicator remains lit forever."]}

### R073 / item_0006 (until_termination)
The state must remain active until a release or a cancellation occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a cancellation occurs"}
{"review_id": "R073", "comments": "Open interpretation only.", "interpretations": ["The state remains active until the first of a release or a cancellation occurs.", "Either a release or a cancellation ends the active-state obligation; neither event is explicitly required."]}

### R074 / item_0007 (until_termination)
The state must remain active until a release occurs while the indicator is lit.
{"a": "the state is active", "b": "a release occurs", "c": "the indicator is lit"}
{"review_id": "R074", "comments": "Open interpretation only.", "interpretations": ["The state remains active until a release occurs at a step when the indicator is lit.", "The terminating release must coincide with the indicator being lit."]}

### R075 / item_0008 (until_termination)
The state must remain active until the indicator stays lit permanently.
{"a": "the state is active", "b": "the indicator is lit"}
{"review_id": "R075", "comments": "Open interpretation only.", "interpretations": ["The state remains active until a point from which the indicator stays lit forever.", "Permanent illumination of the indicator ends the active-state obligation."]}

### R076 / item_0009 (until_termination)
Whenever a request occurs, starting at the next step the state must remain active until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a request occurs"}
{"review_id": "R076", "comments": "Open interpretation only.", "interpretations": ["For every request at step t, the state must remain active starting at step t plus one until a release occurs.", "The request itself does not require the state to be active at the request step, only from the next step onward."]}

### R077 / item_0010 (until_termination)
Until a release occurs, every pulse must be followed by a flash at the next step.
{"a": "a pulse occurs", "b": "a release occurs", "c": "a flash occurs"}
{"review_id": "R077", "comments": "Open interpretation only.", "interpretations": ["Before the first release, every pulse must be followed by a flash exactly at the next step.", "After the release occurs, the pulse-to-next-step-flash obligation no longer applies."]}

### R078 / item_0011 (until_termination)
The first state must remain active until a handoff starts a second phase in which the second state remains active and a release must eventually end that phase.
{"a": "the first state is active", "b": "a handoff occurs", "c": "the second state is active", "d": "a release occurs"}
{"review_id": "R078", "comments": "Open interpretation only.", "interpretations": ["The first state remains active until a handoff occurs; after the handoff, the second state remains active until a release, and that release must eventually occur.", "The behavior is a two-phase sequence: first-state active, handoff, second-state active, mandatory release."]}

### R079 / item_0012 (until_termination)
A handoff must eventually occur with the first state active beforehand; from that handoff the second state must remain active until a release occurs.
{"a": "the first state is active", "b": "a handoff occurs", "c": "the second state is active", "d": "a release occurs"}
{"review_id": "R079", "comments": "Open interpretation only.", "interpretations": ["A handoff must eventually occur, with the first state active before it; from the handoff onward, the second state remains active until a release occurs.", "The handoff is mandatory, the second state obligation starts at the handoff, and a release eventually ends it."]}

### R080 / item_0001 (order_scope)
A pulse is to be followed later by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R080", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, a flash must occur at some strictly later step.", "There exists a pulse that is followed later by a flash."]}

### R081 / item_0002 (order_scope)
After a pulse, the light is to stay on from the next step onward.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R081", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs at step t, the light is on for every step after t and remains on forever.", "A pulse triggers permanent light-on starting at the next step."]}

### R082 / item_0003 (order_scope)
After a pulse, the light is to settle into staying on at some later step.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R082", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, there is some later step from which the light becomes on and remains on forever.", "The light may fluctuate before settling, but after the pulse it eventually enters a permanently on state."]}

### R083 / item_0004 (order_scope)
A pulse is to be followed later by a flash and, later still, a chime.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a chime occurs"}
{"review_id": "R083", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, a flash occurs later, and then a chime occurs later than that flash.", "The required order is pulse, then flash, then chime."]}

### R084 / item_0005 (order_scope)
After a pulse, a flash is to occur later with no pulse in between.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R084", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs at step t, a flash occurs at some later step t prime, and no pulse occurs between t and t prime.", "The required flash must come before any subsequent pulse."]}

### R085 / item_0006 (order_scope)
After a pulse, a flash is to occur later without a pause in between.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a pause state holds"}
{"review_id": "R085", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs at step t, a flash occurs at some later step t prime, and no pause state holds between t and t prime.", "The required flash must occur before any pause after the pulse."]}

### R086 / item_0007 (order_scope)
After a pulse, the next release is to occur with the light on.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R086", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs, the first later release occurs while the light is on.", "The light need not remain on continuously, but it must be on at the next release after the pulse."]}

### R087 / item_0008 (order_scope)
A pulse while enabled is to be followed later by a flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "an enable state holds"}
{"review_id": "R087", "comments": "Open interpretation only.", "interpretations": ["Whenever a pulse occurs while the enable state holds, a flash must occur at some strictly later step.", "Only enabled pulses create a later-flash obligation; disabled pulses are unconstrained."]}

### R088 / item_0009 (order_scope)
Before the first stop, a pulse is to be followed later by a flash, also before that stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R088", "comments": "Open interpretation only.", "interpretations": ["For every pulse before the first stop, a flash must occur later than the pulse but before that first stop.", "The required flash must be strictly between the pulse and the first stop."]}

## Stage 2

### R001
[{"reading_id": "a", "plain": "At least one step has both events."}, {"reading_id": "b", "plain": "Each event occurs at least once, possibly at different steps."}]
{"review_id": "R001", "comments": "Conjunction can be read jointly or distributively.", "additional_interpretations": ["The pulse and flash may occur in either order."], "supports": {"a": "Supported", "b": "Supported"}}

### R002
[{"reading_id": "a", "plain": "Both events coincide infinitely often."}, {"reading_id": "b", "plain": "Each event occurs infinitely often, without required coincidence."}]
{"review_id": "R002", "comments": "Plural keep occurring favors separate recurrence, not coincidence.", "additional_interpretations": ["Pulses and flashes may alternate but need not be paired."], "supports": {"a": "Not supported", "b": "Supported"}}

### R003
[{"reading_id": "a", "plain": "Every request has a strictly later step with both events."}, {"reading_id": "b", "plain": "Every request has a strictly later pulse and a strictly later flash, possibly at different steps."}]
{"review_id": "R003", "comments": "Followed by a pulse and a flash may be joint or separate.", "additional_interpretations": ["The pulse and flash after a request may occur in either order."], "supports": {"a": "Supported", "b": "Supported"}}

### R004
[{"reading_id": "a", "plain": "A joint occurrence is required before the first stop, if a stop occurs."}, {"reading_id": "b", "plain": "Each event is required before the first stop, at possibly different steps."}]
{"review_id": "R004", "comments": "Both events before a stop can be read jointly or separately.", "additional_interpretations": ["If no stop ever occurs, the requirement may be vacuous or still demand eventual pulse and flash."], "supports": {"a": "Supported", "b": "Supported"}}

### R005
[{"reading_id": "a", "plain": "Starting strictly after each request, both events must coincide before any subsequent stop."}, {"reading_id": "b", "plain": "Starting strictly after each request, each event must occur before any subsequent stop, possibly separately."}]
{"review_id": "R005", "comments": "Before the next stop can allow joint or separate events.", "additional_interpretations": ["If no subsequent stop exists, the pulse and flash are still eventually required after the request."], "supports": {"a": "Supported", "b": "Supported"}}

### R006
[{"reading_id": "a", "plain": "Both states hold throughout the same pair of consecutive steps."}, {"reading_id": "b", "plain": "Each state has a pair of consecutive active steps, possibly different pairs."}]
{"review_id": "R006", "comments": "The phrasing favors a common two-step active episode.", "additional_interpretations": ["The two consecutive steps must be a common active episode for both signal and indicator."], "supports": {"a": "Supported", "b": "Not supported"}}

### R007
[{"reading_id": "a", "plain": "At some step both are inactive and at the next both are active."}, {"reading_id": "b", "plain": "Each independently changes from inactive to active at least once."}]
{"review_id": "R007", "comments": "Become active does not require a common inactive-to-active transition.", "additional_interpretations": ["They may become active at different times and without a common preceding inactive step."], "supports": {"a": "Not supported", "b": "Supported"}}

### R008
[{"reading_id": "a", "plain": "A common episode starts with both active and maintains both until a release occurs."}, {"reading_id": "b", "plain": "Each has its own active episode lasting until a release, possibly different episodes and releases."}]
{"review_id": "R008", "comments": "Active until a release favors a common joint episode.", "additional_interpretations": ["The release is common to the joint active episode."], "supports": {"a": "Supported", "b": "Not supported"}}

### R009
[{"reading_id": "a", "plain": "A joint pulse-and-flash step occurs with a strictly later completion."}, {"reading_id": "b", "plain": "Each event occurs with some strictly later completion, possibly separately."}]
{"review_id": "R009", "comments": "Pulse and flash with completion may be joint or separate.", "additional_interpretations": ["Pulse and flash need not be simultaneous; completion is after them."], "supports": {"a": "Supported", "b": "Supported"}}

### R010
[{"reading_id": "a", "plain": "Some start precedes a joint occurrence, which precedes a finish."}, {"reading_id": "b", "plain": "Some start precedes both events, which may occur separately before a finish."}]
{"review_id": "R010", "comments": "After start and before finish can allow joint or separate events.", "additional_interpretations": ["Pulse and flash may occur in either order between start and finish."], "supports": {"a": "Supported", "b": "Supported"}}

### R011
[{"reading_id": "a", "plain": "The two two-step sequences have the same starting step."}, {"reading_id": "b", "plain": "Each two-step sequence occurs, possibly starting at different steps."}]
{"review_id": "R011", "comments": "Same starting step is possible but not clearly favored.", "additional_interpretations": ["The two sequences may overlap, be simultaneous, or occur at different times."], "supports": {"a": "Uncertain", "b": "Supported"}}

### R012
[{"reading_id": "a", "plain": "There are infinitely many starting steps for a common two-step active episode."}, {"reading_id": "b", "plain": "Each has infinitely many two-step active episodes, with no required alignment."}]
{"review_id": "R012", "comments": "Keep being active for two consecutive steps favors joint recurring episodes.", "additional_interpretations": ["Recurring joint two-step active episodes are required."], "supports": {"a": "Supported", "b": "Not supported"}}

### R013
[{"reading_id": "a", "plain": "A flash occurs exactly one step after each pulse."}, {"reading_id": "b", "plain": "A flash occurs at some strictly later step after each pulse."}]
{"review_id": "R013", "comments": "Followed by can mean immediate or later.", "additional_interpretations": ["Followed by may be immediate or merely later."], "supports": {"a": "Supported", "b": "Supported"}}

### R014
[{"reading_id": "a", "plain": "A pulse at the current step requires a flash at the next step."}, {"reading_id": "b", "plain": "A pulse at the current step requires a flash at some later step."}]
{"review_id": "R014", "comments": "If pulse now, flash may be immediate or later.", "additional_interpretations": ["If pulse now, flash may be immediate or later."], "supports": {"a": "Supported", "b": "Supported"}}

### R015
[{"reading_id": "a", "plain": "Some pulse has a flash at the next step."}, {"reading_id": "b", "plain": "Some pulse has a flash at a strictly later step."}]
{"review_id": "R015", "comments": "At least one pulse followed by a flash can be adjacent or delayed.", "additional_interpretations": ["At least one pulse-flash pair; adjacency not fixed."], "supports": {"a": "Supported", "b": "Supported"}}

### R016
[{"reading_id": "a", "plain": "The indicator is on at every step beginning at the next step after each pulse."}, {"reading_id": "b", "plain": "After each pulse, there is a later step from which the indicator is always on."}]
{"review_id": "R016", "comments": "Then stay on permanently favors immediate permanent activation.", "additional_interpretations": ["No delay or flicker is permitted after the pulse."], "supports": {"a": "Supported", "b": "Not supported"}}

### R017
[{"reading_id": "a", "plain": "The first stop eventually occurs, and every earlier pulse has a flash at its next step."}, {"reading_id": "b", "plain": "The first stop eventually occurs, and every earlier pulse has a flash at some strictly later step."}]
{"review_id": "R017", "comments": "Flash after stop suggests later, not necessarily next step.", "additional_interpretations": ["Flash may occur after the first stop; only pulses before first stop are constrained."], "supports": {"a": "Uncertain", "b": "Supported"}}

### R018
[{"reading_id": "a", "plain": "Each pulse has a flash at the next step, and a chime occurs later than that flash."}, {"reading_id": "b", "plain": "Each pulse has a flash at some later step, and a chime occurs still later."}]
{"review_id": "R018", "comments": "Pulse-to-flash timing is not fixed; chime is strictly after flash.", "additional_interpretations": ["Chime must be strictly after the flash, not merely after pulse."], "supports": {"a": "Supported", "b": "Supported"}}

### R019
[{"reading_id": "a", "plain": "No pulse has a flash at the next step."}, {"reading_id": "b", "plain": "No pulse has a flash at any strictly later step."}]
{"review_id": "R019", "comments": "Never followed favors no later flash at all.", "additional_interpretations": ["Flashes before pulses are allowed; flashes after pulses are forbidden."], "supports": {"a": "Not supported", "b": "Supported"}}

### R020
[{"reading_id": "a", "plain": "Each pulse has a flash without a stop at the next step."}, {"reading_id": "b", "plain": "Each pulse has a later flash, with no stop from the next step through that flash step."}]
{"review_id": "R020", "comments": "Later flash before stop is clear; immediate flash is stricter.", "additional_interpretations": ["Flash step itself must not coincide with stop."], "supports": {"a": "Uncertain", "b": "Supported"}}

### R021
[{"reading_id": "a", "plain": "Each consecutive pulse pair has a flash at the step immediately after its second pulse."}, {"reading_id": "b", "plain": "Each consecutive pulse pair has a flash at some strictly later step than its second pulse."}]
{"review_id": "R021", "comments": "Followed by may be immediate or later after the pair.", "additional_interpretations": ["Trigger is consecutive pulse pair; flash after second pulse not necessarily immediate."], "supports": {"a": "Supported", "b": "Supported"}}

### R022
[{"reading_id": "a", "plain": "There is a step after which every pulse has a flash at the next step."}, {"reading_id": "b", "plain": "There is a step after which every pulse has a flash at some strictly later step."}]
{"review_id": "R022", "comments": "The eventual rule does not specify immediate flash.", "additional_interpretations": ["Before eventual step, pulses may be unfulfilled."], "supports": {"a": "Uncertain", "b": "Supported"}}

### R023
[{"reading_id": "a", "plain": "Infinitely many pulses have a flash at the next step."}, {"reading_id": "b", "plain": "Infinitely many pulses have a flash at some strictly later step."}]
{"review_id": "R023", "comments": "Over and over can allow adjacent or delayed pairs.", "additional_interpretations": ["Repetition may have variable spacing."], "supports": {"a": "Supported", "b": "Supported"}}

### R024
[{"reading_id": "a", "plain": "Beginning at the first activation step, every pulse has a flash at the next step."}, {"reading_id": "b", "plain": "Beginning at the first activation step, every pulse has a flash at some strictly later step."}]
{"review_id": "R024", "comments": "Activation starts universal rule; timing of flash is not fixed.", "additional_interpretations": ["Pulses before activation unconstrained."], "supports": {"a": "Uncertain", "b": "Supported"}}

### R025
[{"reading_id": "a", "plain": "Every request has an active response at its own step."}, {"reading_id": "b", "plain": "Every request has an active response at some strictly later step."}]
{"review_id": "R025", "comments": "Require can mean same-step or later response.", "additional_interpretations": ["Response may be simultaneous or delayed."], "supports": {"a": "Supported", "b": "Supported"}}

### R026
[{"reading_id": "a", "plain": "A starting-step request requires the response at the starting step."}, {"reading_id": "b", "plain": "A starting-step request requires the response strictly later."}]
{"review_id": "R026", "comments": "Only the starting-step request is constrained; response timing ambiguous.", "additional_interpretations": ["Only initial-step request triggers; response timing ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R027
[{"reading_id": "a", "plain": "Some request coincides with an active response."}, {"reading_id": "b", "plain": "Some request has an active response strictly later."}]
{"review_id": "R027", "comments": "Existential request with response can be simultaneous or later.", "additional_interpretations": ["Existential; no universal requirement."], "supports": {"a": "Supported", "b": "Supported"}}

### R028
[{"reading_id": "a", "plain": "Infinitely many requests coincide with an active response."}, {"reading_id": "b", "plain": "Infinitely many requests have an active response strictly later."}]
{"review_id": "R028", "comments": "Keep occurring can allow simultaneous or delayed responses.", "additional_interpretations": ["Keep occurring means infinitely many request-response episodes."], "supports": {"a": "Supported", "b": "Supported"}}

### R029
[{"reading_id": "a", "plain": "From some point onward, each request coincides with an active response."}, {"reading_id": "b", "plain": "From some point onward, each request has an active response strictly later."}]
{"review_id": "R029", "comments": "Eventually always can allow simultaneous or delayed responses.", "additional_interpretations": ["Eventually stable universal requirement."], "supports": {"a": "Supported", "b": "Supported"}}

### R030
[{"reading_id": "a", "plain": "Before the first release, every request coincides with an active response; a release occurs."}, {"reading_id": "b", "plain": "Before the first release, every request has an active response strictly later; a release occurs."}]
{"review_id": "R030", "comments": "Same-step response is clear; strictly later may cross release.", "additional_interpretations": ["Active response should occur while pre-release obligation is in force."], "supports": {"a": "Supported", "b": "Uncertain"}}

### R031
[{"reading_id": "a", "plain": "Every request before the first release, or forever if no release occurs, coincides with an active response."}, {"reading_id": "b", "plain": "Every request before the first release, or forever if no release occurs, has an active response strictly later."}]
{"review_id": "R031", "comments": "Same-step response is clear; strictly later timing is ambiguous.", "additional_interpretations": ["Active response should occur while obligation is in force."], "supports": {"a": "Supported", "b": "Uncertain"}}

### R032
[{"reading_id": "a", "plain": "At and after the first release, every request coincides with an active response."}, {"reading_id": "b", "plain": "At and after the first release, every request has an active response strictly later."}]
{"review_id": "R032", "comments": "From release onward can allow simultaneous or delayed responses.", "additional_interpretations": ["Requests before first release are unconstrained."], "supports": {"a": "Supported", "b": "Supported"}}

### R033
[{"reading_id": "a", "plain": "For each request, the response is active from the request step forever."}, {"reading_id": "b", "plain": "For each request, the response is active forever starting at some strictly later step."}]
{"review_id": "R033", "comments": "Remains active forever can start same-step or later.", "additional_interpretations": ["Response may begin at request step or later, then never deactivate."], "supports": {"a": "Supported", "b": "Supported"}}

### R034
[{"reading_id": "a", "plain": "Each request starts a requirement for activity at that step and until a release occurs."}, {"reading_id": "b", "plain": "Each request has a strictly later step starting a requirement for activity then and until a release occurs."}]
{"review_id": "R034", "comments": "Stay active until release can start same-step or later.", "additional_interpretations": ["Release must occur after each request's active interval."], "supports": {"a": "Supported", "b": "Supported"}}

### R035
[{"reading_id": "a", "plain": "A request exactly one step from the start requires a response at that same step."}, {"reading_id": "b", "plain": "A request exactly one step from the start requires a response at some step after it."}]
{"review_id": "R035", "comments": "Next-step request triggers; response timing ambiguous.", "additional_interpretations": ["Request at step one triggers; response timing ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R036
[{"reading_id": "a", "plain": "Every request made when permission holds coincides with an active response."}, {"reading_id": "b", "plain": "Every request made when permission holds has an active response strictly later."}]
{"review_id": "R036", "comments": "Permission condition at request step; response timing ambiguous.", "additional_interpretations": ["Permission condition evaluated at request step."], "supports": {"a": "Supported", "b": "Supported"}}

### R037
[{"reading_id": "a", "plain": "At least one qualifying pulse has a flash at that step or some later step."}, {"reading_id": "b", "plain": "Every qualifying pulse has a flash at that step or some later step; no pulse is required."}]
{"review_id": "R037", "comments": "Generic rule favors universal, not existential.", "additional_interpretations": ["If no pulse occurs, requirement vacuously satisfied."], "supports": {"a": "Not supported", "b": "Supported"}}

### R038
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on at its step."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on at its step; no pulse is required."}]
{"review_id": "R038", "comments": "Requires favors universal conditional.", "additional_interpretations": ["No existence requirement."], "supports": {"a": "Not supported", "b": "Supported"}}

### R039
[{"reading_id": "a", "plain": "At least one qualifying pulse has a flash exactly one step afterward."}, {"reading_id": "b", "plain": "Every qualifying pulse has a flash exactly one step afterward; no pulse is required."}]
{"review_id": "R039", "comments": "Is to have favors universal rule.", "additional_interpretations": ["Flash exactly next step for every pulse."], "supports": {"a": "Not supported", "b": "Supported"}}

### R040
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on at that step and every subsequent step."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on at that step and every subsequent step; no pulse is required."}]
{"review_id": "R040", "comments": "Requires favors universal rule.", "additional_interpretations": ["Permanent light-on from pulse step onward."], "supports": {"a": "Not supported", "b": "Supported"}}

### R041
[{"reading_id": "a", "plain": "At least one qualifying pulse has a release at or after its step and the light on at every step from the pulse up to but excluding that release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a release at or after its step and the light on at every step from the pulse up to but excluding that release; no pulse is required."}]
{"review_id": "R041", "comments": "Calls for favors universal obligation.", "additional_interpretations": ["Release required for each pulse obligation."], "supports": {"a": "Not supported", "b": "Supported"}}

### R042
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on from its step until just before a release, or forever if there is no release."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on from its step until just before a release, or forever if there is no release; no pulse is required."}]
{"review_id": "R042", "comments": "Calls for favors universal weak-until obligation.", "additional_interpretations": ["Weak until: no release means forever."], "supports": {"a": "Not supported", "b": "Supported"}}

### R043
[{"reading_id": "a", "plain": "At least one qualifying pulse has a first release at or after its step, with the light on at that release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a first release at or after its step, with the light on at that release; no pulse is required."}]
{"review_id": "R043", "comments": "Calls for favors universal obligation.", "additional_interpretations": ["Only first release after pulse matters."], "supports": {"a": "Not supported", "b": "Supported"}}

### R044
[{"reading_id": "a", "plain": "At least one qualifying pulse has a release at or after its step, no flashes before that release from the pulse onward, and a flash at or after the release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a release at or after its step, no flashes before that release from the pulse onward, and a flash at or after the release; no pulse is required."}]
{"review_id": "R044", "comments": "Calls for favors universal ordering obligation.", "additional_interpretations": ["Order pulse, release, flash; no flash before release."], "supports": {"a": "Not supported", "b": "Supported"}}

### R045
[{"reading_id": "a", "plain": "At least one qualifying pulse occurs while enabled and has a flash at that step or later."}, {"reading_id": "b", "plain": "Every qualifying pulse occurs while enabled and has a flash at that step or later; no pulse is required."}]
{"review_id": "R045", "comments": "While enabled calls for favors universal conditional.", "additional_interpretations": ["Enable state at pulse step only."], "supports": {"a": "Not supported", "b": "Supported"}}

### R046
[{"reading_id": "a", "plain": "At least one qualifying pulse occurs strictly before the first stop, if any, and has a flash at its step or later."}, {"reading_id": "b", "plain": "Every qualifying pulse occurs strictly before the first stop, if any, and has a flash at its step or later; no pulse is required."}]
{"review_id": "R046", "comments": "Before first stop calls for favors universal conditional.", "additional_interpretations": ["If no stop occurs, reading may be vacuous or apply to all pulses depending on weak or strong until."], "supports": {"a": "Not supported", "b": "Supported"}}

### R047
[{"reading_id": "a", "plain": "At the current step, at least one indicator is inactive."}, {"reading_id": "b", "plain": "At the current step, each indicator is inactive."}]
{"review_id": "R047", "comments": "Must not be active means both inactive.", "additional_interpretations": ["No constraint on future steps."], "supports": {"a": "Not supported", "b": "Supported"}}

### R048
[{"reading_id": "a", "plain": "At every step, at least one indicator is inactive."}, {"reading_id": "b", "plain": "At every step, each indicator is inactive."}]
{"review_id": "R048", "comments": "Never be active means both inactive at every step.", "additional_interpretations": ["Neither indicator ever active."], "supports": {"a": "Not supported", "b": "Supported"}}

### R049
[{"reading_id": "a", "plain": "Some step has at least one inactive indicator."}, {"reading_id": "b", "plain": "Some step has each indicator inactive."}]
{"review_id": "R049", "comments": "At some point not active means both inactive at that point.", "additional_interpretations": ["Some step with both inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R050
[{"reading_id": "a", "plain": "Infinitely many steps have at least one inactive indicator."}, {"reading_id": "b", "plain": "Infinitely many steps have each indicator inactive."}]
{"review_id": "R050", "comments": "Infinitely often not active means both inactive infinitely often.", "additional_interpretations": ["Infinitely many steps with both inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R051
[{"reading_id": "a", "plain": "Eventually every remaining step has at least one inactive indicator, with the inactive indicator allowed to vary."}, {"reading_id": "b", "plain": "Eventually each indicator stays inactive forever."}]
{"review_id": "R051", "comments": "From some point onward not active means both inactive thereafter.", "additional_interpretations": ["After some point, both remain inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R052
[{"reading_id": "a", "plain": "A release eventually occurs; at each earlier step at least one indicator is inactive."}, {"reading_id": "b", "plain": "A release eventually occurs; at each earlier step each indicator is inactive."}]
{"review_id": "R052", "comments": "Not active until release means both inactive before release.", "additional_interpretations": ["Release required; before it both inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R053
[{"reading_id": "a", "plain": "Before the first release, at least one indicator is inactive at every step; if no release occurs this lasts forever."}, {"reading_id": "b", "plain": "Before the first release, each indicator is inactive at every step; if no release occurs this lasts forever."}]
{"review_id": "R053", "comments": "Not active until optional release means both inactive before first release.", "additional_interpretations": ["Release optional; before first release both inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R054
[{"reading_id": "a", "plain": "Every open-gate step has at least one inactive indicator."}, {"reading_id": "b", "plain": "Every open-gate step has each indicator inactive."}]
{"review_id": "R054", "comments": "Whenever gate open, both must not be active.", "additional_interpretations": ["Open gate forbids either indicator active."], "supports": {"a": "Not supported", "b": "Supported"}}

### R055
[{"reading_id": "a", "plain": "The step immediately after every pulse has at least one inactive indicator."}, {"reading_id": "b", "plain": "The step immediately after every pulse has each indicator inactive."}]
{"review_id": "R055", "comments": "Immediately following step must have both inactive.", "additional_interpretations": ["Immediately after pulse, both inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R056
[{"reading_id": "a", "plain": "Every pulse has a current or later step with at least one inactive indicator."}, {"reading_id": "b", "plain": "Every pulse has a current or later step with each indicator inactive."}]
{"review_id": "R056", "comments": "Step at that time or later when both are not active.", "additional_interpretations": ["Some step at or after pulse with both inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R057
[{"reading_id": "a", "plain": "Each pulse requires a current or later release, with at least one indicator inactive at every step from the pulse up to but excluding that release."}, {"reading_id": "b", "plain": "Each pulse requires a current or later release, with each indicator inactive at every step from the pulse up to but excluding that release."}]
{"review_id": "R057", "comments": "Both inactive until required release.", "additional_interpretations": ["Release required; both inactive from pulse until release."], "supports": {"a": "Not supported", "b": "Supported"}}

### R058
[{"reading_id": "a", "plain": "Some check occurs with at least one indicator inactive."}, {"reading_id": "b", "plain": "Some check occurs with each indicator inactive."}]
{"review_id": "R058", "comments": "Check occurs when both are not active.", "additional_interpretations": ["Check step must have both inactive."], "supports": {"a": "Not supported", "b": "Supported"}}

### R059
[{"reading_id": "a", "plain": "One response type answers every request at its own step."}, {"reading_id": "b", "plain": "Each request has a response at its own step, with the type allowed to vary."}]
{"review_id": "R059", "comments": "Pulse or flash allows varying type, not one fixed type.", "additional_interpretations": ["Disjunction allows varying response type; not necessarily same type for all."], "supports": {"a": "Not supported", "b": "Supported"}}

### R060
[{"reading_id": "a", "plain": "One response type is required at the step immediately after every request."}, {"reading_id": "b", "plain": "The step immediately after each request has either response type, with the type allowed to vary."}]
{"review_id": "R060", "comments": "Next step pulse or flash allows varying type.", "additional_interpretations": ["Next-step response type can vary."], "supports": {"a": "Not supported", "b": "Supported"}}

### R061
[{"reading_id": "a", "plain": "The same sole response type occurs at every request step."}, {"reading_id": "b", "plain": "Exactly one response occurs at each request step, and the chosen type can change."}]
{"review_id": "R061", "comments": "At once but not both allows varying sole response.", "additional_interpretations": ["Exactly one at same step; type may vary."], "supports": {"a": "Not supported", "b": "Supported"}}

### R062
[{"reading_id": "a", "plain": "One event ordering applies to every request, starting at its step."}, {"reading_id": "b", "plain": "Each request begins either ordering, and the ordering can vary."}]
{"review_id": "R062", "comments": "Either ordering can vary per request.", "additional_interpretations": ["Ordering can vary per request; two events on consecutive steps."], "supports": {"a": "Not supported", "b": "Supported"}}

### R063
[{"reading_id": "a", "plain": "One signal is required from each request until a release; every request must reach a release."}, {"reading_id": "b", "plain": "Each request chooses a signal to maintain until a release, and every request must reach a release."}]
{"review_id": "R063", "comments": "First or second signal can be chosen per request.", "additional_interpretations": ["Choice of first or second signal per request; release eventually for each."], "supports": {"a": "Not supported", "b": "Supported"}}

### R064
[{"reading_id": "a", "plain": "One signal serves all requests and stays active until release, or forever if no release occurs."}, {"reading_id": "b", "plain": "A signal is chosen per request and maintained until release, or forever without release."}]
{"review_id": "R064", "comments": "First or second signal can be chosen per request; release optional.", "additional_interpretations": ["Choice per request; release optional."], "supports": {"a": "Not supported", "b": "Supported"}}

### R065
[{"reading_id": "a", "plain": "Before a required stop, one response type answers all requests at their own steps."}, {"reading_id": "b", "plain": "Before a required stop, requests receive same-step responses whose types can vary."}]
{"review_id": "R065", "comments": "Immediate pulse or flash allows varying type before required stop.", "additional_interpretations": ["Immediate same-step response before mandatory stop; type varies."], "supports": {"a": "Not supported", "b": "Supported"}}

### R066
[{"reading_id": "a", "plain": "One response type answers all requests before the first stop, or forever if there is no stop."}, {"reading_id": "b", "plain": "Response types may vary among requests before the first stop, or forever without a stop."}]
{"review_id": "R066", "comments": "Immediate pulse or flash allows varying type unless stop.", "additional_interpretations": ["Immediate same-step response unless stop; type varies."], "supports": {"a": "Not supported", "b": "Supported"}}

### R067
[{"reading_id": "a", "plain": "One response type must occur for every request before any stop at or after that request."}, {"reading_id": "b", "plain": "Each request must get either response type before a stop, with types allowed to vary."}]
{"review_id": "R067", "comments": "Pulse or flash before next stop allows varying type.", "additional_interpretations": ["Response before next stop; type varies."], "supports": {"a": "Not supported", "b": "Supported"}}

### R068
[{"reading_id": "a", "plain": "A release eventually occurs, and the state is active at every earlier step."}, {"reading_id": "b", "plain": "The state stays active before a release; if no release occurs, it stays active forever."}]
{"review_id": "R068", "comments": "Until release is ambiguous between strong and weak until.", "additional_interpretations": ["Strong versus weak until; release may or may not be required."], "supports": {"a": "Supported", "b": "Supported"}}

### R069
[{"reading_id": "a", "plain": "Every request has a release at that step or later, with activity at each intervening step."}, {"reading_id": "b", "plain": "Every request requires activity before a release, or forever if none follows."}]
{"review_id": "R069", "comments": "Whenever request, until release is ambiguous.", "additional_interpretations": ["Per request, release may be required or optional."], "supports": {"a": "Supported", "b": "Supported"}}

### R070
[{"reading_id": "a", "plain": "Some step starts an activity interval ending in a release, possibly immediately."}, {"reading_id": "b", "plain": "Some step starts an activity interval ending in a release or continuing forever."}]
{"review_id": "R070", "comments": "Eventually until release is ambiguous.", "additional_interpretations": ["Eventually some interval; strong or weak until ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R071
[{"reading_id": "a", "plain": "At each step a release is still forthcoming, and activity holds before it."}, {"reading_id": "b", "plain": "At each step activity holds before the next release, and forever if releases stop."}]
{"review_id": "R071", "comments": "From every step onward until release is ambiguous.", "additional_interpretations": ["Global obligation from every step; release timing ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R072
[{"reading_id": "a", "plain": "Both maintained conditions hold before an eventual release."}, {"reading_id": "b", "plain": "Both maintained conditions hold before a release, or forever without one."}]
{"review_id": "R072", "comments": "Both conditions until release is ambiguous.", "additional_interpretations": ["Both conditions maintained jointly until release; release optional or required ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R073
[{"reading_id": "a", "plain": "At least one terminating event eventually occurs, with prior activity."}, {"reading_id": "b", "plain": "Activity persists until either terminating event, or forever if neither occurs."}]
{"review_id": "R073", "comments": "Until release or cancellation is ambiguous.", "additional_interpretations": ["Either release or cancellation terminates; eventual termination ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R074
[{"reading_id": "a", "plain": "A release with a lit indicator eventually occurs, with activity before that joint condition."}, {"reading_id": "b", "plain": "Activity lasts until a release with a lit indicator, or forever if that combination never occurs."}]
{"review_id": "R074", "comments": "Until release while lit is ambiguous.", "additional_interpretations": ["Terminating release must coincide with lit indicator; eventual occurrence ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R075
[{"reading_id": "a", "plain": "The indicator eventually becomes permanently lit, with activity before a qualifying start."}, {"reading_id": "b", "plain": "Activity continues until permanent illumination starts, or forever if it never does."}]
{"review_id": "R075", "comments": "Until permanent illumination is ambiguous.", "additional_interpretations": ["Permanent illumination is terminator; eventual occurrence ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R076
[{"reading_id": "a", "plain": "Every request initiates a next-step interval that must end in a release."}, {"reading_id": "b", "plain": "Every request initiates a next-step interval that may persist without release."}]
{"review_id": "R076", "comments": "Next-step interval until release is ambiguous.", "additional_interpretations": ["Interval starts at next step; release eventual or optional ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R077
[{"reading_id": "a", "plain": "A release eventually occurs; pulses before it require next-step flashes."}, {"reading_id": "b", "plain": "Pulses before a release require next-step flashes; without a release this rule applies forever."}]
{"review_id": "R077", "comments": "Until release rule is ambiguous.", "additional_interpretations": ["Rule applies until release; release eventual or optional ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R078
[{"reading_id": "a", "plain": "A qualifying handoff eventually occurs and begins a second phase with mandatory release."}, {"reading_id": "b", "plain": "A qualifying handoff may never occur if the first state remains active forever; if it occurs the second phase has mandatory release."}]
{"review_id": "R078", "comments": "Handoff may be required or optional, but release in second phase is mandatory.", "additional_interpretations": ["Handoff may be required or optional depending on until; second phase release mandatory."], "supports": {"a": "Supported", "b": "Supported"}}

### R079
[{"reading_id": "a", "plain": "A handoff and then a release occur, with the corresponding state active before each endpoint."}, {"reading_id": "b", "plain": "A handoff occurs, after which the second state may remain active forever without release."}]
{"review_id": "R079", "comments": "Handoff is mandatory; release terminator is ambiguous.", "additional_interpretations": ["Handoff mandatory; release terminator eventual or optional ambiguous."], "supports": {"a": "Supported", "b": "Supported"}}

### R080
[{"reading_id": "a", "plain": "At least one pulse must occur with a flash at a strictly later step."}, {"reading_id": "b", "plain": "Every pulse must have a flash at a strictly later step; pulses need not occur."}]
{"review_id": "R080", "comments": "Generic rule favors universal conditional.", "additional_interpretations": ["Universal conditional; no pulse existence required."], "supports": {"a": "Not supported", "b": "Supported"}}

### R081
[{"reading_id": "a", "plain": "At least one pulse must occur after which the light is on at every step starting with the next step."}, {"reading_id": "b", "plain": "After every pulse, the light must be on at every step starting with the next step; pulses need not occur."}]
{"review_id": "R081", "comments": "After a pulse favors universal rule.", "additional_interpretations": ["Light on from next step forever after every pulse."], "supports": {"a": "Not supported", "b": "Supported"}}

### R082
[{"reading_id": "a", "plain": "At least one pulse must occur, and at some strictly later step the light must begin remaining on forever."}, {"reading_id": "b", "plain": "For every pulse, there must be a strictly later step from which the light stays on forever; pulses need not occur."}]
{"review_id": "R082", "comments": "After a pulse favors universal settling rule.", "additional_interpretations": ["Settling point may vary per pulse."], "supports": {"a": "Not supported", "b": "Supported"}}

### R083
[{"reading_id": "a", "plain": "At least one pulse must occur with a later flash and a chime strictly later than that flash."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash and a chime strictly later than that flash; pulses need not occur."}]
{"review_id": "R083", "comments": "A pulse is to be followed favors universal sequence.", "additional_interpretations": ["Strict order pulse, flash, chime."], "supports": {"a": "Not supported", "b": "Supported"}}

### R084
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later flash and no pulse strictly between them; a pulse at the flash step is allowed."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash with no pulse strictly between them; a pulse at the flash step is allowed, and pulses need not occur."}]
{"review_id": "R084", "comments": "After a pulse favors universal no-pulse-between rule.", "additional_interpretations": ["No intervening pulse between pulse and required flash."], "supports": {"a": "Not supported", "b": "Supported"}}

### R085
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later flash and no pause state strictly between them; pause states at the endpoints are allowed."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash with no pause state strictly between them; pause states at the endpoints are allowed, and pulses need not occur."}]
{"review_id": "R085", "comments": "After a pulse favors universal no-pause-between rule.", "additional_interpretations": ["No intervening pause state; endpoints may pause."], "supports": {"a": "Not supported", "b": "Supported"}}

### R086
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later release, and the light must be on at the first release strictly after that pulse."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later release, and the light must be on at the first release strictly after it; pulses need not occur."}]
{"review_id": "R086", "comments": "After a pulse favors universal next-release rule.", "additional_interpretations": ["Next release after pulse must have light on."], "supports": {"a": "Not supported", "b": "Supported"}}

### R087
[{"reading_id": "a", "plain": "At least one pulse must occur while enabled and have a strictly later flash; the enable state need not persist."}, {"reading_id": "b", "plain": "Every pulse occurring while enabled must have a strictly later flash; the enable state need not persist and enabled pulses need not occur."}]
{"review_id": "R087", "comments": "Pulse while enabled favors universal conditional.", "additional_interpretations": ["Enable state at pulse step; flash later."], "supports": {"a": "Not supported", "b": "Supported"}}

### R088
[{"reading_id": "a", "plain": "At least one pulse must occur and have a strictly later flash, both before the first stop; if no stop occurs both events must still occur."}, {"reading_id": "b", "plain": "Every pulse before the first stop must have a strictly later flash before that stop; if no stop occurs apply this rule forever, and pulses need not occur."}]
{"review_id": "R088", "comments": "Before first stop favors universal bounded rule.", "additional_interpretations": ["Flash must occur before same first stop as pulse; if no stop, rule may apply forever."], "supports": {"a": "Not supported", "b": "Supported"}}
