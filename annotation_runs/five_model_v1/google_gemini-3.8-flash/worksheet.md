# Model-generated annotation worksheet
Model: google/gemini-3.8-flash
Times below are actual orchestration timestamps (UTC).
Stage 1 started: 2026-11-03T23:25:58.203531+00:00; completed: 2026-11-03T23:26:36.674963+00:00
Stage 2 started: 2026-11-03T23:26:36.683452+00:00; completed: 2026-11-03T23:27:23.571775+00:00

## Stage 1 (frozen)

### R001 / item_0001 (joint_separate)
A pulse and a flash must eventually occur.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R001", "comments": "", "interpretations": ["Eventually, both a pulse occurs and a flash occurs, possibly at different times.", "Eventually, a step occurs where both a pulse and a flash occur simultaneously."]}

### R002 / item_0002 (joint_separate)
Pulses and flashes must keep occurring.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R002", "comments": "", "interpretations": ["Pulses occur infinitely often and flashes occur infinitely often.", "Steps where both a pulse and a flash occur together happen infinitely often."]}

### R003 / item_0003 (joint_separate)
Every request must be followed by a pulse and a flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a request occurs"}
{"review_id": "R003", "comments": "", "interpretations": ["Whenever a request occurs, there must eventually be a pulse and eventually be a flash at or after the request.", "Whenever a request occurs, there must be a later step where both a pulse and a flash occur simultaneously.", "Whenever a request occurs, it must be followed by a pulse and then subsequently a flash."]}

### R004 / item_0004 (joint_separate)
A pulse and a flash must occur before any stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R004", "comments": "", "interpretations": ["If a stop ever occurs, both a pulse and a flash must occur strictly before the first stop.", "A stop must eventually occur, preceded by both a pulse and a flash.", "Both a pulse and a flash must occur at or before any stop."]}

### R005 / item_0005 (joint_separate)
After each request, a pulse and a flash are required before the next stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a request occurs", "d": "a stop occurs"}
{"review_id": "R005", "comments": "", "interpretations": ["For every request, before the next stop occurs, both a pulse and a flash must occur.", "Whenever a request occurs, if a stop follows, a pulse and a flash must occur between the request and that stop."]}

### R006 / item_0006 (joint_separate)
The signal and the indicator must eventually be active for two consecutive steps.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R006", "comments": "", "interpretations": ["Eventually, there are two consecutive steps during which both the signal and the indicator are active.", "Eventually, the signal is active for two consecutive steps and the indicator is active for two consecutive steps, possibly at different times."]}

### R007 / item_0007 (joint_separate)
The signal and the indicator must eventually become active.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R007", "comments": "", "interpretations": ["Eventually the signal becomes active and eventually the indicator becomes active.", "Eventually there is a step where both the signal and the indicator become active simultaneously."]}

### R008 / item_0008 (joint_separate)
Eventually the signal and the indicator must be active until a release occurs.
{"a": "a signal is active", "b": "an indicator is active", "c": "a release occurs"}
{"review_id": "R008", "comments": "", "interpretations": ["Eventually, a time is reached from which both the signal and the indicator remain continuously active until a release occurs.", "Eventually both the signal and the indicator are active, and each remains active until a release occurs."]}

### R009 / item_0009 (joint_separate)
A pulse and a flash must occur with a completion afterward.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a completion occurs"}
{"review_id": "R009", "comments": "", "interpretations": ["A pulse and a flash must occur, followed strictly later by a completion.", "A pulse and a flash must eventually occur, and at or after both have occurred, a completion occurs."]}

### R010 / item_0010 (joint_separate)
After a start, a pulse and a flash must occur before a finish.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a start occurs", "d": "a finish occurs"}
{"review_id": "R010", "comments": "", "interpretations": ["After any start, both a pulse and a flash must occur before the next finish.", "Following a start, there must eventually be a pulse and a flash prior to a finish occurring."]}

### R011 / item_0011 (joint_separate)
A pulse immediately followed by a flash and a click immediately followed by a mark must eventually occur.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a click occurs", "d": "a mark appears"}
{"review_id": "R011", "comments": "", "interpretations": ["Eventually there is a pulse immediately followed by a flash, and eventually there is a click immediately followed by a mark.", "Eventually there is a step where a pulse and a click occur simultaneously, followed immediately by both a flash and a mark."]}

### R012 / item_0012 (joint_separate)
The signal and the indicator must keep being active for two consecutive steps.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R012", "comments": "", "interpretations": ["Infinitely often, both the signal and the indicator are active across two consecutive steps.", "Both the signal and the indicator remain active together across every pair of consecutive steps permanently."]}

### R013 / item_0001 (next_later)
Every pulse must be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R013", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur at some point at or after that pulse.", "Whenever a pulse occurs, a flash must occur at some strictly later step."]}

### R014 / item_0002 (next_later)
If there is a pulse now, a flash must follow.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R014", "comments": "", "interpretations": ["If a pulse occurs at the initial step, a flash must occur at some later step.", "If a pulse occurs at the current step, a flash must occur at or after that step."]}

### R015 / item_0003 (next_later)
There must be at least one pulse followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R015", "comments": "", "interpretations": ["There exists at least one pulse that is followed at a later step by a flash.", "There exists at least one pulse that is followed at or after that step by a flash."]}

### R016 / item_0004 (next_later)
After every pulse, the indicator must then stay on permanently.
{"a": "a pulse occurs", "b": "the indicator is on"}
{"review_id": "R016", "comments": "", "interpretations": ["Whenever a pulse occurs, the indicator must be active permanently from that step onward.", "Whenever a pulse occurs, the indicator must be active permanently starting from the next step onward."]}

### R017 / item_0005 (next_later)
A stop must occur, and before the first stop every pulse must be followed by a flash, even if that flash comes after the stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R017", "comments": "", "interpretations": ["A stop must occur, and every pulse occurring prior to the first stop must eventually be followed by a flash, even if the flash occurs after the stop.", "A stop is guaranteed to happen, and all pulses before that stop must have a corresponding flash at or after the pulse."]}

### R018 / item_0006 (next_later)
Every pulse must be followed by a flash, with a chime at some strictly later step than that flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a chime occurs"}
{"review_id": "R018", "comments": "", "interpretations": ["Whenever a pulse occurs, it must be followed by a flash, and strictly after that flash a chime must occur.", "Whenever a pulse occurs, there is a subsequent flash and a chime that occurs at a strictly later step than that flash."]}

### R019 / item_0007 (next_later)
A pulse must never be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R019", "comments": "", "interpretations": ["No flash may ever occur at or after any pulse.", "No flash may ever occur strictly after a pulse."]}

### R020 / item_0008 (next_later)
Every pulse must be followed by a flash before any subsequent stop, with no stop at the flash step.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R020", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur before any subsequent stop, and no stop can occur on the step of the flash.", "Every pulse must be followed by a flash strictly before the next stop, with stop being false at the step of the flash."]}

### R021 / item_0009 (next_later)
Every pair of pulses on consecutive steps must be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R021", "comments": "", "interpretations": ["Whenever a pulse occurs on two consecutive steps, a flash must eventually occur at or after the second pulse.", "Whenever a pulse occurs on two consecutive steps, a flash must occur strictly after the second pulse."]}

### R022 / item_0010 (next_later)
Eventually, the rule that every pulse is followed by a flash must hold from then on.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R022", "comments": "", "interpretations": ["There is some point in time after which every pulse that occurs is followed by a flash.", "Eventually the property holds globally that any pulse is followed by a flash."]}

### R023 / item_0011 (next_later)
A pulse followed by a flash must occur over and over without end.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R023", "comments": "", "interpretations": ["Infinitely often, a pulse occurs that is subsequently followed by a flash.", "A sequence of a pulse followed by a flash repeats indefinitely."]}

### R024 / item_0012 (next_later)
Once an activation occurs, every pulse from that step onward must be followed by a flash.
{"a": "an activation occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R024", "comments": "", "interpretations": ["After the first occurrence of an activation, every pulse that occurs from that step onward must be followed by a flash.", "Once an activation occurs, all pulses from the next step onward must be followed by a flash."]}

### R025 / item_0001 (same_later)
Requests require an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R025", "comments": "", "interpretations": ["Whenever a request occurs, the response must be active at that same step.", "Whenever a request occurs, the response must eventually become active at or after the request."]}

### R026 / item_0002 (same_later)
A request at the starting step requires an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R026", "comments": "", "interpretations": ["If a request occurs at step 0, the response must be active at step 0.", "If a request occurs at step 0, the response must eventually become active."]}

### R027 / item_0003 (same_later)
There must be a request with an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R027", "comments": "", "interpretations": ["There must exist a step where a request occurs and the response is active.", "There must exist a request that eventually receives an active response."]}

### R028 / item_0004 (same_later)
Requests with an active response must keep occurring.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R028", "comments": "", "interpretations": ["Steps where a request occurs and the response is active must occur infinitely often.", "Requests must keep occurring, each accompanied or followed by an active response."]}

### R029 / item_0005 (same_later)
Eventually, requests must always have an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R029", "comments": "", "interpretations": ["Eventually, a point is reached from which every request has an active response at that step.", "Eventually, every request that occurs is followed by an active response."]}

### R030 / item_0006 (same_later)
Requests require an active response until a release occurs, and a release must occur.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R030", "comments": "", "interpretations": ["A release must occur, and until that release, any request must have an active response.", "Every request requires an active response until a release occurs, and a release is guaranteed to happen."]}

### R031 / item_0007 (same_later)
Requests require an active response unless and until a release occurs.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R031", "comments": "", "interpretations": ["Until a release occurs, every request must have an active response; if no release occurs, this requirement holds forever.", "Requests require an active response unless a release has occurred."]}

### R032 / item_0008 (same_later)
From the first release onward, requests require an active response.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R032", "comments": "", "interpretations": ["From the first step where a release occurs onward, whenever a request occurs, the response must be active.", "Once a release occurs, all future requests require an active response."]}

### R033 / item_0009 (same_later)
Every request requires a response that remains active forever.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R033", "comments": "", "interpretations": ["Whenever a request occurs, the response must be active from that step onward permanently.", "Whenever a request occurs, the response must become active and remain active forever."]}

### R034 / item_0010 (same_later)
Every request requires the response to stay active until a release, which must occur.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R034", "comments": "", "interpretations": ["Whenever a request occurs, the response must remain active until a release occurs, and a release must eventually occur.", "Each request requires the response to stay continuously active until a mandatory release."]}

### R035 / item_0011 (same_later)
A request at the next step requires an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R035", "comments": "", "interpretations": ["If a request occurs at the next step, the response must be active at that next step.", "If a request occurs at the next step, the response must eventually be active."]}

### R036 / item_0012 (same_later)
Requests made while the response is permitted require an active response.
{"a": "a request occurs", "b": "the response is active", "c": "the response is permitted"}
{"review_id": "R036", "comments": "", "interpretations": ["Whenever a request occurs while the response is permitted, the response must be active at that step.", "Whenever a request occurs while the response is permitted, an active response must follow."]}

### R037 / item_0001 (trigger_scope_final)
A pulse is to be followed by a flash, possibly at the same step.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R037", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur at the same step or at some later step.", "Every pulse must eventually be accompanied or followed by a flash."]}

### R038 / item_0002 (trigger_scope_final)
A pulse requires the light to be on at that step.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R038", "comments": "", "interpretations": ["Whenever a pulse occurs, the light must be on at that exact step.", "At any step with a pulse, the light is on."]}

### R039 / item_0003 (trigger_scope_final)
A pulse is to have a flash at the next step.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R039", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur at the immediately following step.", "Each pulse must be followed by a flash on the next time step."]}

### R040 / item_0004 (trigger_scope_final)
A pulse requires the light to stay on from that step onward.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R040", "comments": "", "interpretations": ["Whenever a pulse occurs, the light must stay on permanently from that step onward.", "Every pulse causes the light to remain on indefinitely starting at that step."]}

### R041 / item_0005 (trigger_scope_final)
A pulse calls for the light to be on until a release occurs, with a release required.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R041", "comments": "", "interpretations": ["Whenever a pulse occurs, the light must be on continuously until a release occurs, and a release must eventually occur.", "A pulse requires the light to stay on until a release, which is guaranteed to occur at or after the pulse."]}

### R042 / item_0006 (trigger_scope_final)
A pulse calls for the light to stay on until a release, or forever if no release comes.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R042", "comments": "", "interpretations": ["Whenever a pulse occurs, the light must remain on until a release occurs, or forever if no release ever occurs.", "A pulse requires the light to stay on weakly until a release."]}

### R043 / item_0007 (trigger_scope_final)
A pulse calls for the light to be on at the first release at or after that pulse, and that release must occur.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R043", "comments": "", "interpretations": ["Whenever a pulse occurs, a release must eventually occur at or after that pulse, and the light must be on at the first such release.", "For each pulse, a release is required, and the light must be on at that release step."]}

### R044 / item_0008 (trigger_scope_final)
A pulse calls for a release before any flash from that step onward, and a flash at or after the release.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a release occurs"}
{"review_id": "R044", "comments": "", "interpretations": ["Whenever a pulse occurs, a release must occur before any flash at or after the pulse, and a flash must eventually occur at or after the release.", "A pulse requires that no flash occurs until after a release, followed eventually by a flash."]}

### R045 / item_0009 (trigger_scope_final)
A pulse while enabled calls for a flash at that step or later.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "an enable state holds"}
{"review_id": "R045", "comments": "", "interpretations": ["Whenever a pulse occurs while the enable state holds, a flash must occur at that step or later.", "If a pulse occurs during an enable state, a flash must eventually occur."]}

### R046 / item_0010 (trigger_scope_final)
Before the first stop, a pulse calls for a flash at that step or later.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R046", "comments": "", "interpretations": ["For any pulse occurring before the first stop, a flash must occur at or after that pulse.", "Before any stop occurs, any pulse requires a flash at that step or later."]}

### R047 / item_0001 (negation_scope)
The first and second indicators must not be active now.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R047", "comments": "", "interpretations": ["At the current step, neither the first indicator nor the second indicator is active.", "At step 0, both the first and second indicators must be inactive."]}

### R048 / item_0002 (negation_scope)
The first and second indicators must never be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R048", "comments": "", "interpretations": ["Neither the first indicator nor the second indicator is ever active at any time step.", "Both indicators must remain inactive globally."]}

### R049 / item_0003 (negation_scope)
At some point, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R049", "comments": "", "interpretations": ["There is some step where neither the first indicator nor the second indicator is active.", "Eventually, both indicators are simultaneously inactive at least once."]}

### R050 / item_0004 (negation_scope)
Infinitely often, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R050", "comments": "", "interpretations": ["Infinitely often, both the first and second indicators are simultaneously inactive.", "There are infinitely many steps where neither indicator is active."]}

### R051 / item_0005 (negation_scope)
From some point onward, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R051", "comments": "", "interpretations": ["Eventually, a point is reached after which neither the first nor the second indicator is ever active.", "From some step onward, both indicators stay inactive permanently."]}

### R052 / item_0006 (negation_scope)
The first and second indicators must not be active until a release occurs, and a release must occur.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a release occurs"}
{"review_id": "R052", "comments": "", "interpretations": ["Neither the first nor the second indicator may be active until a release occurs, and a release must eventually occur.", "Both indicators must remain inactive until a mandatory release."]}

### R053 / item_0007 (negation_scope)
The first and second indicators must not be active until a release occurs; release is optional.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a release occurs"}
{"review_id": "R053", "comments": "", "interpretations": ["Neither the first nor the second indicator may be active until a release occurs; if no release occurs, they remain inactive forever.", "Both indicators stay inactive unless and until a release happens."]}

### R054 / item_0008 (negation_scope)
Whenever the gate is open, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "the gate is open"}
{"review_id": "R054", "comments": "", "interpretations": ["Whenever the gate is open, neither the first nor the second indicator is active at that step.", "At any time the gate is open, both indicators must be inactive."]}

### R055 / item_0009 (negation_scope)
Whenever a pulse occurs, the first and second indicators must not be active at the immediately following step.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs"}
{"review_id": "R055", "comments": "", "interpretations": ["Whenever a pulse occurs, neither the first nor the second indicator may be active at the next step.", "The step immediately following any pulse must have both indicators inactive."]}

### R056 / item_0010 (negation_scope)
Whenever a pulse occurs, there must be a step at that time or later when the first and second indicators are not active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs"}
{"review_id": "R056", "comments": "", "interpretations": ["Whenever a pulse occurs, there must eventually be a step at or after the pulse where neither indicator is active.", "For every pulse, a state where both indicators are inactive will eventually occur."]}

### R057 / item_0011 (negation_scope)
Whenever a pulse occurs, the first and second indicators must not be active until a release occurs at that step or later, and such a release is required.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs", "d": "a release occurs"}
{"review_id": "R057", "comments": "", "interpretations": ["Whenever a pulse occurs, neither indicator may be active until a release occurs at or after that step, and such a release is required.", "Each pulse requires both indicators to be inactive until a subsequent mandatory release."]}

### R058 / item_0012 (negation_scope)
A check must occur at a step when the first and second indicators are not active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a check occurs"}
{"review_id": "R058", "comments": "", "interpretations": ["Eventually a check must occur at a step where neither the first nor the second indicator is active.", "There must be an occurrence of a check with both indicators simultaneously inactive."]}

### R059 / item_0001 (or_scope)
Requests are answered by a pulse or a flash.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R059", "comments": "", "interpretations": ["Whenever a request occurs, either a pulse or a flash must eventually occur at or after that request.", "Whenever a request occurs, either a pulse or a flash must occur at that same step."]}

### R060 / item_0002 (or_scope)
After a request, the next step must contain a pulse or a flash.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R060", "comments": "", "interpretations": ["Whenever a request occurs, either a pulse or a flash must occur at the next step.", "After each request, the immediately following step must contain a pulse, a flash, or both."]}

### R061 / item_0003 (or_scope)
A request must be answered at once by a pulse or a flash, but not both.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R061", "comments": "", "interpretations": ["Whenever a request occurs, exactly one of a pulse or a flash must occur at that exact step.", "A request requires an immediate response of either a pulse or a flash, but not both at the same time."]}

### R062 / item_0004 (or_scope)
Every request starts a pulse-then-flash or flash-then-pulse response, with the two events on consecutive steps.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R062", "comments": "", "interpretations": ["Every request must be followed by a pulse and then immediately a flash, or a flash and then immediately a pulse.", "Whenever a request occurs, it triggers either a pulse followed on the next step by a flash, or a flash followed on the next step by a pulse."]}

### R063 / item_0005 (or_scope)
A request requires the first or second signal to stay active until a release, which must eventually occur.
{"a": "a request occurs", "b": "the first signal is active", "c": "the second signal is active", "d": "a release occurs"}
{"review_id": "R063", "comments": "", "interpretations": ["Whenever a request occurs, at least one of the signals must remain continuously active until a release occurs, and a release must eventually occur.", "Each request requires the first signal or the second signal to stay active until a mandatory release."]}

### R064 / item_0006 (or_scope)
A request requires the first or second signal to remain active unless released; release is optional.
{"a": "a request occurs", "b": "the first signal is active", "c": "the second signal is active", "d": "a release occurs"}
{"review_id": "R064", "comments": "", "interpretations": ["Whenever a request occurs, the first signal or the second signal must remain active until a release occurs, or forever if no release occurs.", "Requests require either the first or second signal to stay active unless released."]}

### R065 / item_0007 (or_scope)
Until a stop occurs, requests must receive an immediate pulse or flash; a stop must eventually occur.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R065", "comments": "", "interpretations": ["A stop must eventually occur, and until that stop, every request must receive an immediate pulse or flash.", "Every request occurring before the first stop must immediately be accompanied by a pulse or flash, with a stop guaranteed to happen."]}

### R066 / item_0008 (or_scope)
Unless a stop occurs, requests must receive an immediate pulse or flash; a stop is not required.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R066", "comments": "", "interpretations": ["Until a stop occurs (if ever), every request must receive an immediate pulse or flash.", "If no stop occurs, requests must always receive an immediate pulse or flash; a stop is optional."]}

### R067 / item_0009 (or_scope)
Requests must receive a pulse or flash before the next stop.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R067", "comments": "", "interpretations": ["Whenever a request occurs, a pulse or a flash must occur before the next stop occurs.", "For each request, before any subsequent stop, a pulse or flash must take place."]}

### R068 / item_0001 (until_termination)
The state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R068", "comments": "", "interpretations": ["The state must remain active until a release occurs.", "The state stays active until a mandatory release occurs.", "The state stays active until a release occurs, release being optional."]}

### R069 / item_0002 (until_termination)
Whenever a request occurs, the state must remain active until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a request occurs"}
{"review_id": "R069", "comments": "", "interpretations": ["Whenever a request occurs, the state must remain active from that step until a release occurs.", "Every request requires the state to be active until a release occurs."]}

### R070 / item_0003 (until_termination)
Eventually, the state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R070", "comments": "", "interpretations": ["Eventually, a step is reached from which the state remains active until a release occurs.", "At some future point, the state stays active until a release occurs."]}

### R071 / item_0004 (until_termination)
From every step onward, the state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R071", "comments": "", "interpretations": ["At every step, the state must remain active until a release occurs.", "From any time step onward, the state must stay active until a release happens."]}

### R072 / item_0005 (until_termination)
The state must remain active and the indicator lit until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "the indicator is lit"}
{"review_id": "R072", "comments": "", "interpretations": ["Both the state must be active and the indicator lit until a release occurs.", "The state remains active and the indicator lit continuously until a release happens."]}

### R073 / item_0006 (until_termination)
The state must remain active until a release or a cancellation occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a cancellation occurs"}
{"review_id": "R073", "comments": "", "interpretations": ["The state must remain active until either a release occurs or a cancellation occurs.", "The state stays active until the first occurrence of a release or cancellation."]}

### R074 / item_0007 (until_termination)
The state must remain active until a release occurs while the indicator is lit.
{"a": "the state is active", "b": "a release occurs", "c": "the indicator is lit"}
{"review_id": "R074", "comments": "", "interpretations": ["The state must remain active until a step occurs where both a release occurs and the indicator is lit.", "The state stays active until a release happens while the indicator is lit."]}

### R075 / item_0008 (until_termination)
The state must remain active until the indicator stays lit permanently.
{"a": "the state is active", "b": "the indicator is lit"}
{"review_id": "R075", "comments": "", "interpretations": ["The state must remain active until a point from which the indicator stays lit permanently.", "The state is active until the indicator enters a permanently lit condition."]}

### R076 / item_0009 (until_termination)
Whenever a request occurs, starting at the next step the state must remain active until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a request occurs"}
{"review_id": "R076", "comments": "", "interpretations": ["Whenever a request occurs, starting at the next step the state must remain active until a release occurs.", "After any request, the state must be active from the next step until a release."]}

### R077 / item_0010 (until_termination)
Until a release occurs, every pulse must be followed by a flash at the next step.
{"a": "a pulse occurs", "b": "a release occurs", "c": "a flash occurs"}
{"review_id": "R077", "comments": "", "interpretations": ["Before any release occurs, every pulse must be followed by a flash at the next step.", "Until a release happens, any pulse must have a flash at the immediately following step."]}

### R078 / item_0011 (until_termination)
The first state must remain active until a handoff starts a second phase in which the second state remains active and a release must eventually end that phase.
{"a": "the first state is active", "b": "a handoff occurs", "c": "the second state is active", "d": "a release occurs"}
{"review_id": "R078", "comments": "", "interpretations": ["The first state must remain active until a handoff occurs, after which the second state remains active until a mandatory release ends it.", "The first state stays active until a handoff, which starts a phase where the second state stays active until a release occurs."]}

### R079 / item_0012 (until_termination)
A handoff must eventually occur with the first state active beforehand; from that handoff the second state must remain active until a release occurs.
{"a": "the first state is active", "b": "a handoff occurs", "c": "the second state is active", "d": "a release occurs"}
{"review_id": "R079", "comments": "", "interpretations": ["A handoff must eventually occur with the first state active up to that handoff, and from that handoff the second state must remain active until a release occurs.", "Eventually a handoff occurs preceded by the first state being active, after which the second state stays active until a release."]}

### R080 / item_0001 (order_scope)
A pulse is to be followed later by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R080", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur at a strictly later step.", "A pulse must be followed at some subsequent time by a flash."]}

### R081 / item_0002 (order_scope)
After a pulse, the light is to stay on from the next step onward.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R081", "comments": "", "interpretations": ["Whenever a pulse occurs, the light must stay on permanently from the next step onward.", "After any pulse, the light remains on for all subsequent steps."]}

### R082 / item_0003 (order_scope)
After a pulse, the light is to settle into staying on at some later step.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R082", "comments": "", "interpretations": ["Whenever a pulse occurs, there must eventually be a step after which the light stays on permanently.", "After a pulse, the light eventually becomes permanently on."]}

### R083 / item_0004 (order_scope)
A pulse is to be followed later by a flash and, later still, a chime.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a chime occurs"}
{"review_id": "R083", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur at a strictly later step, and a chime must occur strictly after that flash.", "A pulse is followed by a later flash, which in turn is followed by an even later chime."]}

### R084 / item_0005 (order_scope)
After a pulse, a flash is to occur later with no pulse in between.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R084", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur at a later step with no pulse occurring in between the two.", "After a pulse, the next pulse must not occur before a flash occurs."]}

### R085 / item_0006 (order_scope)
After a pulse, a flash is to occur later without a pause in between.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a pause state holds"}
{"review_id": "R085", "comments": "", "interpretations": ["Whenever a pulse occurs, a flash must occur at a later step, and the pause state must not hold at any step strictly between them.", "After a pulse, a flash occurs later without any intervening pause state."]}

### R086 / item_0007 (order_scope)
After a pulse, the next release is to occur with the light on.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R086", "comments": "", "interpretations": ["Whenever a pulse occurs, the very next release must occur at a step where the light is on.", "After a pulse, the first subsequent release must happen with the light on."]}

### R087 / item_0008 (order_scope)
A pulse while enabled is to be followed later by a flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "an enable state holds"}
{"review_id": "R087", "comments": "", "interpretations": ["Whenever a pulse occurs while enabled, a flash must occur at a strictly later step.", "A pulse during an enable state must be followed later by a flash."]}

### R088 / item_0009 (order_scope)
Before the first stop, a pulse is to be followed later by a flash, also before that stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R088", "comments": "", "interpretations": ["For any pulse occurring before the first stop, a flash must occur strictly after that pulse and also strictly before that first stop.", "Before the first stop occurs, any pulse must be followed by a flash that also precedes that stop."]}

## Stage 2

### R001
[{"reading_id": "a", "plain": "At least one step has both events."}, {"reading_id": "b", "plain": "Each event occurs at least once, possibly at different steps."}]
{"review_id": "R001", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R002
[{"reading_id": "a", "plain": "Both events coincide infinitely often."}, {"reading_id": "b", "plain": "Each event occurs infinitely often, without required coincidence."}]
{"review_id": "R002", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R003
[{"reading_id": "a", "plain": "Every request has a strictly later step with both events."}, {"reading_id": "b", "plain": "Every request has a strictly later pulse and a strictly later flash, possibly at different steps."}]
{"review_id": "R003", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R004
[{"reading_id": "a", "plain": "A joint occurrence is required before the first stop, if a stop occurs."}, {"reading_id": "b", "plain": "Each event is required before the first stop, at possibly different steps."}]
{"review_id": "R004", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R005
[{"reading_id": "a", "plain": "Starting strictly after each request, both events must coincide before any subsequent stop."}, {"reading_id": "b", "plain": "Starting strictly after each request, each event must occur before any subsequent stop, possibly separately."}]
{"review_id": "R005", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R006
[{"reading_id": "a", "plain": "Both states hold throughout the same pair of consecutive steps."}, {"reading_id": "b", "plain": "Each state has a pair of consecutive active steps, possibly different pairs."}]
{"review_id": "R006", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R007
[{"reading_id": "a", "plain": "At some step both are inactive and at the next both are active."}, {"reading_id": "b", "plain": "Each independently changes from inactive to active at least once."}]
{"review_id": "R007", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R008
[{"reading_id": "a", "plain": "A common episode starts with both active and maintains both until a release occurs."}, {"reading_id": "b", "plain": "Each has its own active episode lasting until a release, possibly different episodes and releases."}]
{"review_id": "R008", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R009
[{"reading_id": "a", "plain": "A joint pulse-and-flash step occurs with a strictly later completion."}, {"reading_id": "b", "plain": "Each event occurs with some strictly later completion, possibly separately."}]
{"review_id": "R009", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R010
[{"reading_id": "a", "plain": "Some start precedes a joint occurrence, which precedes a finish."}, {"reading_id": "b", "plain": "Some start precedes both events, which may occur separately before a finish."}]
{"review_id": "R010", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R011
[{"reading_id": "a", "plain": "The two two-step sequences have the same starting step."}, {"reading_id": "b", "plain": "Each two-step sequence occurs, possibly starting at different steps."}]
{"review_id": "R011", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R012
[{"reading_id": "a", "plain": "There are infinitely many starting steps for a common two-step active episode."}, {"reading_id": "b", "plain": "Each has infinitely many two-step active episodes, with no required alignment."}]
{"review_id": "R012", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R013
[{"reading_id": "a", "plain": "A flash occurs exactly one step after each pulse."}, {"reading_id": "b", "plain": "A flash occurs at some strictly later step after each pulse."}]
{"review_id": "R013", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R014
[{"reading_id": "a", "plain": "A pulse at the current step requires a flash at the next step."}, {"reading_id": "b", "plain": "A pulse at the current step requires a flash at some later step."}]
{"review_id": "R014", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R015
[{"reading_id": "a", "plain": "Some pulse has a flash at the next step."}, {"reading_id": "b", "plain": "Some pulse has a flash at a strictly later step."}]
{"review_id": "R015", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R016
[{"reading_id": "a", "plain": "The indicator is on at every step beginning at the next step after each pulse."}, {"reading_id": "b", "plain": "After each pulse, there is a later step from which the indicator is always on."}]
{"review_id": "R016", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R017
[{"reading_id": "a", "plain": "The first stop eventually occurs, and every earlier pulse has a flash at its next step."}, {"reading_id": "b", "plain": "The first stop eventually occurs, and every earlier pulse has a flash at some strictly later step."}]
{"review_id": "R017", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R018
[{"reading_id": "a", "plain": "Each pulse has a flash at the next step, and a chime occurs later than that flash."}, {"reading_id": "b", "plain": "Each pulse has a flash at some later step, and a chime occurs still later."}]
{"review_id": "R018", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R019
[{"reading_id": "a", "plain": "No pulse has a flash at the next step."}, {"reading_id": "b", "plain": "No pulse has a flash at any strictly later step."}]
{"review_id": "R019", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R020
[{"reading_id": "a", "plain": "Each pulse has a flash without a stop at the next step."}, {"reading_id": "b", "plain": "Each pulse has a later flash, with no stop from the next step through that flash step."}]
{"review_id": "R020", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R021
[{"reading_id": "a", "plain": "Each consecutive pulse pair has a flash at the step immediately after its second pulse."}, {"reading_id": "b", "plain": "Each consecutive pulse pair has a flash at some strictly later step than its second pulse."}]
{"review_id": "R021", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R022
[{"reading_id": "a", "plain": "There is a step after which every pulse has a flash at the next step."}, {"reading_id": "b", "plain": "There is a step after which every pulse has a flash at some strictly later step."}]
{"review_id": "R022", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R023
[{"reading_id": "a", "plain": "Infinitely many pulses have a flash at the next step."}, {"reading_id": "b", "plain": "Infinitely many pulses have a flash at some strictly later step."}]
{"review_id": "R023", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R024
[{"reading_id": "a", "plain": "Beginning at the first activation step, every pulse has a flash at the next step."}, {"reading_id": "b", "plain": "Beginning at the first activation step, every pulse has a flash at some strictly later step."}]
{"review_id": "R024", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R025
[{"reading_id": "a", "plain": "Every request has an active response at its own step."}, {"reading_id": "b", "plain": "Every request has an active response at some strictly later step."}]
{"review_id": "R025", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R026
[{"reading_id": "a", "plain": "A starting-step request requires the response at the starting step."}, {"reading_id": "b", "plain": "A starting-step request requires the response strictly later."}]
{"review_id": "R026", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R027
[{"reading_id": "a", "plain": "Some request coincides with an active response."}, {"reading_id": "b", "plain": "Some request has an active response strictly later."}]
{"review_id": "R027", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R028
[{"reading_id": "a", "plain": "Infinitely many requests coincide with an active response."}, {"reading_id": "b", "plain": "Infinitely many requests have an active response strictly later."}]
{"review_id": "R028", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R029
[{"reading_id": "a", "plain": "From some point onward, each request coincides with an active response."}, {"reading_id": "b", "plain": "From some point onward, each request has an active response strictly later."}]
{"review_id": "R029", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R030
[{"reading_id": "a", "plain": "Before the first release, every request coincides with an active response; a release occurs."}, {"reading_id": "b", "plain": "Before the first release, every request has an active response strictly later; a release occurs."}]
{"review_id": "R030", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R031
[{"reading_id": "a", "plain": "Every request before the first release, or forever if no release occurs, coincides with an active response."}, {"reading_id": "b", "plain": "Every request before the first release, or forever if no release occurs, has an active response strictly later."}]
{"review_id": "R031", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R032
[{"reading_id": "a", "plain": "At and after the first release, every request coincides with an active response."}, {"reading_id": "b", "plain": "At and after the first release, every request has an active response strictly later."}]
{"review_id": "R032", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R033
[{"reading_id": "a", "plain": "For each request, the response is active from the request step forever."}, {"reading_id": "b", "plain": "For each request, the response is active forever starting at some strictly later step."}]
{"review_id": "R033", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R034
[{"reading_id": "a", "plain": "Each request starts a requirement for activity at that step and until a release occurs."}, {"reading_id": "b", "plain": "Each request has a strictly later step starting a requirement for activity then and until a release occurs."}]
{"review_id": "R034", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R035
[{"reading_id": "a", "plain": "A request exactly one step from the start requires a response at that same step."}, {"reading_id": "b", "plain": "A request exactly one step from the start requires a response at some step after it."}]
{"review_id": "R035", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R036
[{"reading_id": "a", "plain": "Every request made when permission holds coincides with an active response."}, {"reading_id": "b", "plain": "Every request made when permission holds has an active response strictly later."}]
{"review_id": "R036", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R037
[{"reading_id": "a", "plain": "At least one qualifying pulse has a flash at that step or some later step."}, {"reading_id": "b", "plain": "Every qualifying pulse has a flash at that step or some later step; no pulse is required."}]
{"review_id": "R037", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R038
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on at its step."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on at its step; no pulse is required."}]
{"review_id": "R038", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R039
[{"reading_id": "a", "plain": "At least one qualifying pulse has a flash exactly one step afterward."}, {"reading_id": "b", "plain": "Every qualifying pulse has a flash exactly one step afterward; no pulse is required."}]
{"review_id": "R039", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R040
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on at that step and every subsequent step."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on at that step and every subsequent step; no pulse is required."}]
{"review_id": "R040", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R041
[{"reading_id": "a", "plain": "At least one qualifying pulse has a release at or after its step and the light on at every step from the pulse up to but excluding that release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a release at or after its step and the light on at every step from the pulse up to but excluding that release; no pulse is required."}]
{"review_id": "R041", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R042
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on from its step until just before a release, or forever if there is no release."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on from its step until just before a release, or forever if there is no release; no pulse is required."}]
{"review_id": "R042", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R043
[{"reading_id": "a", "plain": "At least one qualifying pulse has a first release at or after its step, with the light on at that release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a first release at or after its step, with the light on at that release; no pulse is required."}]
{"review_id": "R043", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R044
[{"reading_id": "a", "plain": "At least one qualifying pulse has a release at or after its step, no flashes before that release from the pulse onward, and a flash at or after the release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a release at or after its step, no flashes before that release from the pulse onward, and a flash at or after the release; no pulse is required."}]
{"review_id": "R044", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R045
[{"reading_id": "a", "plain": "At least one qualifying pulse occurs while enabled and has a flash at that step or later."}, {"reading_id": "b", "plain": "Every qualifying pulse occurs while enabled and has a flash at that step or later; no pulse is required."}]
{"review_id": "R045", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R046
[{"reading_id": "a", "plain": "At least one qualifying pulse occurs strictly before the first stop, if any, and has a flash at its step or later."}, {"reading_id": "b", "plain": "Every qualifying pulse occurs strictly before the first stop, if any, and has a flash at its step or later; no pulse is required."}]
{"review_id": "R046", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R047
[{"reading_id": "a", "plain": "At the current step, at least one indicator is inactive."}, {"reading_id": "b", "plain": "At the current step, each indicator is inactive."}]
{"review_id": "R047", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R048
[{"reading_id": "a", "plain": "At every step, at least one indicator is inactive."}, {"reading_id": "b", "plain": "At every step, each indicator is inactive."}]
{"review_id": "R048", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R049
[{"reading_id": "a", "plain": "Some step has at least one inactive indicator."}, {"reading_id": "b", "plain": "Some step has each indicator inactive."}]
{"review_id": "R049", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R050
[{"reading_id": "a", "plain": "Infinitely many steps have at least one inactive indicator."}, {"reading_id": "b", "plain": "Infinitely many steps have each indicator inactive."}]
{"review_id": "R050", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R051
[{"reading_id": "a", "plain": "Eventually every remaining step has at least one inactive indicator, with the inactive indicator allowed to vary."}, {"reading_id": "b", "plain": "Eventually each indicator stays inactive forever."}]
{"review_id": "R051", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R052
[{"reading_id": "a", "plain": "A release eventually occurs; at each earlier step at least one indicator is inactive."}, {"reading_id": "b", "plain": "A release eventually occurs; at each earlier step each indicator is inactive."}]
{"review_id": "R052", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R053
[{"reading_id": "a", "plain": "Before the first release, at least one indicator is inactive at every step; if no release occurs this lasts forever."}, {"reading_id": "b", "plain": "Before the first release, each indicator is inactive at every step; if no release occurs this lasts forever."}]
{"review_id": "R053", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R054
[{"reading_id": "a", "plain": "Every open-gate step has at least one inactive indicator."}, {"reading_id": "b", "plain": "Every open-gate step has each indicator inactive."}]
{"review_id": "R054", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R055
[{"reading_id": "a", "plain": "The step immediately after every pulse has at least one inactive indicator."}, {"reading_id": "b", "plain": "The step immediately after every pulse has each indicator inactive."}]
{"review_id": "R055", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R056
[{"reading_id": "a", "plain": "Every pulse has a current or later step with at least one inactive indicator."}, {"reading_id": "b", "plain": "Every pulse has a current or later step with each indicator inactive."}]
{"review_id": "R056", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R057
[{"reading_id": "a", "plain": "Each pulse requires a current or later release, with at least one indicator inactive at every step from the pulse up to but excluding that release."}, {"reading_id": "b", "plain": "Each pulse requires a current or later release, with each indicator inactive at every step from the pulse up to but excluding that release."}]
{"review_id": "R057", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R058
[{"reading_id": "a", "plain": "Some check occurs with at least one indicator inactive."}, {"reading_id": "b", "plain": "Some check occurs with each indicator inactive."}]
{"review_id": "R058", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R059
[{"reading_id": "a", "plain": "One response type answers every request at its own step."}, {"reading_id": "b", "plain": "Each request has a response at its own step, with the type allowed to vary."}]
{"review_id": "R059", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R060
[{"reading_id": "a", "plain": "One response type is required at the step immediately after every request."}, {"reading_id": "b", "plain": "The step immediately after each request has either response type, with the type allowed to vary."}]
{"review_id": "R060", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R061
[{"reading_id": "a", "plain": "The same sole response type occurs at every request step."}, {"reading_id": "b", "plain": "Exactly one response occurs at each request step, and the chosen type can change."}]
{"review_id": "R061", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R062
[{"reading_id": "a", "plain": "One event ordering applies to every request, starting at its step."}, {"reading_id": "b", "plain": "Each request begins either ordering, and the ordering can vary."}]
{"review_id": "R062", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R063
[{"reading_id": "a", "plain": "One signal is required from each request until a release; every request must reach a release."}, {"reading_id": "b", "plain": "Each request chooses a signal to maintain until a release, and every request must reach a release."}]
{"review_id": "R063", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R064
[{"reading_id": "a", "plain": "One signal serves all requests and stays active until release, or forever if no release occurs."}, {"reading_id": "b", "plain": "A signal is chosen per request and maintained until release, or forever without release."}]
{"review_id": "R064", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R065
[{"reading_id": "a", "plain": "Before a required stop, one response type answers all requests at their own steps."}, {"reading_id": "b", "plain": "Before a required stop, requests receive same-step responses whose types can vary."}]
{"review_id": "R065", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R066
[{"reading_id": "a", "plain": "One response type answers all requests before the first stop, or forever if there is no stop."}, {"reading_id": "b", "plain": "Response types may vary among requests before the first stop, or forever without a stop."}]
{"review_id": "R066", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R067
[{"reading_id": "a", "plain": "One response type must occur for every request before any stop at or after that request."}, {"reading_id": "b", "plain": "Each request must get either response type before a stop, with types allowed to vary."}]
{"review_id": "R067", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R068
[{"reading_id": "a", "plain": "A release eventually occurs, and the state is active at every earlier step."}, {"reading_id": "b", "plain": "The state stays active before a release; if no release occurs, it stays active forever."}]
{"review_id": "R068", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R069
[{"reading_id": "a", "plain": "Every request has a release at that step or later, with activity at each intervening step."}, {"reading_id": "b", "plain": "Every request requires activity before a release, or forever if none follows."}]
{"review_id": "R069", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R070
[{"reading_id": "a", "plain": "Some step starts an activity interval ending in a release, possibly immediately."}, {"reading_id": "b", "plain": "Some step starts an activity interval ending in a release or continuing forever."}]
{"review_id": "R070", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R071
[{"reading_id": "a", "plain": "At each step a release is still forthcoming, and activity holds before it."}, {"reading_id": "b", "plain": "At each step activity holds before the next release, and forever if releases stop."}]
{"review_id": "R071", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R072
[{"reading_id": "a", "plain": "Both maintained conditions hold before an eventual release."}, {"reading_id": "b", "plain": "Both maintained conditions hold before a release, or forever without one."}]
{"review_id": "R072", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R073
[{"reading_id": "a", "plain": "At least one terminating event eventually occurs, with prior activity."}, {"reading_id": "b", "plain": "Activity persists until either terminating event, or forever if neither occurs."}]
{"review_id": "R073", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R074
[{"reading_id": "a", "plain": "A release with a lit indicator eventually occurs, with activity before that joint condition."}, {"reading_id": "b", "plain": "Activity lasts until a release with a lit indicator, or forever if that combination never occurs."}]
{"review_id": "R074", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R075
[{"reading_id": "a", "plain": "The indicator eventually becomes permanently lit, with activity before a qualifying start."}, {"reading_id": "b", "plain": "Activity continues until permanent illumination starts, or forever if it never does."}]
{"review_id": "R075", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R076
[{"reading_id": "a", "plain": "Every request initiates a next-step interval that must end in a release."}, {"reading_id": "b", "plain": "Every request initiates a next-step interval that may persist without release."}]
{"review_id": "R076", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R077
[{"reading_id": "a", "plain": "A release eventually occurs; pulses before it require next-step flashes."}, {"reading_id": "b", "plain": "Pulses before a release require next-step flashes; without a release this rule applies forever."}]
{"review_id": "R077", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R078
[{"reading_id": "a", "plain": "A qualifying handoff eventually occurs and begins a second phase with mandatory release."}, {"reading_id": "b", "plain": "A qualifying handoff may never occur if the first state remains active forever; if it occurs the second phase has mandatory release."}]
{"review_id": "R078", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R079
[{"reading_id": "a", "plain": "A handoff and then a release occur, with the corresponding state active before each endpoint."}, {"reading_id": "b", "plain": "A handoff occurs, after which the second state may remain active forever without release."}]
{"review_id": "R079", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R080
[{"reading_id": "a", "plain": "At least one pulse must occur with a flash at a strictly later step."}, {"reading_id": "b", "plain": "Every pulse must have a flash at a strictly later step; pulses need not occur."}]
{"review_id": "R080", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R081
[{"reading_id": "a", "plain": "At least one pulse must occur after which the light is on at every step starting with the next step."}, {"reading_id": "b", "plain": "After every pulse, the light must be on at every step starting with the next step; pulses need not occur."}]
{"review_id": "R081", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R082
[{"reading_id": "a", "plain": "At least one pulse must occur, and at some strictly later step the light must begin remaining on forever."}, {"reading_id": "b", "plain": "For every pulse, there must be a strictly later step from which the light stays on forever; pulses need not occur."}]
{"review_id": "R082", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R083
[{"reading_id": "a", "plain": "At least one pulse must occur with a later flash and a chime strictly later than that flash."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash and a chime strictly later than that flash; pulses need not occur."}]
{"review_id": "R083", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R084
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later flash and no pulse strictly between them; a pulse at the flash step is allowed."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash with no pulse strictly between them; a pulse at the flash step is allowed, and pulses need not occur."}]
{"review_id": "R084", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R085
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later flash and no pause state strictly between them; pause states at the endpoints are allowed."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash with no pause state strictly between them; pause states at the endpoints are allowed, and pulses need not occur."}]
{"review_id": "R085", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R086
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later release, and the light must be on at the first release strictly after that pulse."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later release, and the light must be on at the first release strictly after it; pulses need not occur."}]
{"review_id": "R086", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R087
[{"reading_id": "a", "plain": "At least one pulse must occur while enabled and have a strictly later flash; the enable state need not persist."}, {"reading_id": "b", "plain": "Every pulse occurring while enabled must have a strictly later flash; the enable state need not persist and enabled pulses need not occur."}]
{"review_id": "R087", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R088
[{"reading_id": "a", "plain": "At least one pulse must occur and have a strictly later flash, both before the first stop; if no stop occurs both events must still occur."}, {"reading_id": "b", "plain": "Every pulse before the first stop must have a strictly later flash before that stop; if no stop occurs apply this rule forever, and pulses need not occur."}]
{"review_id": "R088", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}
