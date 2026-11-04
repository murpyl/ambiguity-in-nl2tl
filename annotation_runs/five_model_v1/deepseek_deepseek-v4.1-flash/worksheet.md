# Model-generated annotation worksheet
Model: deepseek/deepseek-v4.1-flash
Times below are actual orchestration timestamps (UTC).
Stage 1 started: 2026-11-03T23:40:06.316989+00:00; completed: 2026-11-03T23:45:23.283869+00:00
Stage 2 started: 2026-11-03T23:45:23.285566+00:00; completed: 2026-11-03T23:53:40.708739+00:00

## Stage 1 (frozen)

### R001 / item_0001 (joint_separate)
A pulse and a flash must eventually occur.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R001", "comments": "", "interpretations": ["At some future step a pulse occurs and at some possibly different future step a flash occurs; order is unspecified.", "At some single future step both a pulse and a flash occur simultaneously."]}

### R002 / item_0002 (joint_separate)
Pulses and flashes must keep occurring.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R002", "comments": "", "interpretations": ["Infinitely often a pulse occurs and infinitely often a flash occurs, not necessarily paired.", "From every point onward, both a pulse and a flash occur again in the future.", "A pulse and a flash occur together infinitely often."]}

### R003 / item_0003 (joint_separate)
Every request must be followed by a pulse and a flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a request occurs"}
{"review_id": "R003", "comments": "", "interpretations": ["For each request, a pulse occurs later and a flash occurs later; order is unspecified.", "For each request, a pulse and a flash both occur at some later step, possibly the same step.", "For each request, a pulse occurs later and then a flash occurs later."]}

### R004 / item_0004 (joint_separate)
A pulse and a flash must occur before any stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R004", "comments": "", "interpretations": ["If any stop occurs, then before the first stop a pulse and a flash occur; order is unspecified.", "Before every stop, a pulse and a flash occur.", "A pulse and a flash occur before the first stop, but a stop is not required."]}

### R005 / item_0005 (joint_separate)
After each request, a pulse and a flash are required before the next stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a request occurs", "d": "a stop occurs"}
{"review_id": "R005", "comments": "", "interpretations": ["For each request, if a stop occurs afterward, then a pulse and a flash occur after the request and before that next stop.", "For each request, a pulse and a flash occur after it and before any subsequent stop, even if no stop ever occurs.", "For each request, a pulse occurs and then a flash occurs before the next stop."]}

### R006 / item_0006 (joint_separate)
The signal and the indicator must eventually be active for two consecutive steps.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R006", "comments": "", "interpretations": ["At some future pair of consecutive steps, both the signal and the indicator are active at both steps.", "Eventually there is a two-step interval during which the signal and the indicator are both active throughout.", "At some future step both are active, and at the next step both are active again."]}

### R007 / item_0007 (joint_separate)
The signal and the indicator must eventually become active.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R007", "comments": "", "interpretations": ["At some future step both the signal and the indicator are active simultaneously.", "At some future step the signal becomes active and at some possibly different future step the indicator becomes active.", "Each of the signal and the indicator eventually becomes active at least once."]}

### R008 / item_0008 (joint_separate)
Eventually the signal and the indicator must be active until a release occurs.
{"a": "a signal is active", "b": "an indicator is active", "c": "a release occurs"}
{"review_id": "R008", "comments": "", "interpretations": ["At some future point both signal and indicator become active and remain active until a release occurs; release may or may not be required.", "There is a future interval starting when both are active and ending at a release, with both active throughout; release must occur.", "Eventually both are active unless or until a release occurs; if no release occurs, they stay active forever."]}

### R009 / item_0009 (joint_separate)
A pulse and a flash must occur with a completion afterward.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a completion occurs"}
{"review_id": "R009", "comments": "", "interpretations": ["At some future step a pulse and a flash occur, and after both a completion occurs.", "A pulse occurs, then a flash occurs, then a completion occurs in strict order.", "A pulse and a flash occur, and a completion occurs at some later step than the later of the two."]}

### R010 / item_0010 (joint_separate)
After a start, a pulse and a flash must occur before a finish.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a start occurs", "d": "a finish occurs"}
{"review_id": "R010", "comments": "", "interpretations": ["For each start, if a finish occurs afterward, then a pulse and a flash occur after the start and before that finish.", "For each start, a pulse and a flash occur after it and before the next finish.", "After any start, a pulse and a flash occur before any subsequent finish; order is unspecified."]}

### R011 / item_0011 (joint_separate)
A pulse immediately followed by a flash and a click immediately followed by a mark must eventually occur.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a click occurs", "d": "a mark appears"}
{"review_id": "R011", "comments": "", "interpretations": ["At some future point a pulse occurs and the next step is a flash; separately, at some future point a click occurs and the next step is a mark.", "At some future point both immediate pairs occur, possibly at different times; order between the pairs is unspecified.", "Eventually there is a pulse-flash consecutive pair and a click-mark consecutive pair."]}

### R012 / item_0012 (joint_separate)
The signal and the indicator must keep being active for two consecutive steps.
{"a": "a signal is active", "b": "an indicator is active"}
{"review_id": "R012", "comments": "", "interpretations": ["Infinitely often there is a pair of consecutive steps at which both signal and indicator are active at both steps.", "From every point onward, eventually there is a two-consecutive-step interval where both are active.", "The signal and indicator remain active for two consecutive steps repeatedly forever."]}

### R013 / item_0001 (next_later)
Every pulse must be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R013", "comments": "", "interpretations": ["For every pulse, a flash occurs at some later step.", "For every pulse, a flash occurs at the next step.", "For every pulse, a flash occurs at the same step or later."]}

### R014 / item_0002 (next_later)
If there is a pulse now, a flash must follow.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R014", "comments": "", "interpretations": ["At any step where a pulse occurs, a flash occurs at some later step.", "At any step where a pulse occurs, a flash occurs at the next step.", "At any step where a pulse occurs, a flash occurs at that same step or later."]}

### R015 / item_0003 (next_later)
There must be at least one pulse followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R015", "comments": "", "interpretations": ["At some future step a pulse occurs and at a later step a flash occurs.", "There exists a pulse and a flash with the pulse before the flash.", "At some future step a pulse and a flash occur with the flash at the same or a later step."]}

### R016 / item_0004 (next_later)
After every pulse, the indicator must then stay on permanently.
{"a": "a pulse occurs", "b": "the indicator is on"}
{"review_id": "R016", "comments": "", "interpretations": ["For every pulse, from the next step onward the indicator is on forever.", "For every pulse, from that same step onward the indicator is on forever.", "After the first pulse, the indicator stays on forever."]}

### R017 / item_0005 (next_later)
A stop must occur, and before the first stop every pulse must be followed by a flash, even if that flash comes after the stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R017", "comments": "", "interpretations": ["A stop occurs; for every pulse before the first stop, a flash occurs at some later step, possibly after the first stop.", "A stop occurs; for every pulse before the first stop, a flash occurs eventually after the pulse with no restriction relative to the stop.", "A stop occurs; for every pulse before the first stop, a flash occurs at some step, and pulses after the stop are unconstrained."]}

### R018 / item_0006 (next_later)
Every pulse must be followed by a flash, with a chime at some strictly later step than that flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a chime occurs"}
{"review_id": "R018", "comments": "", "interpretations": ["For every pulse, a flash occurs later than the pulse and a chime occurs strictly later than that flash.", "For every pulse, a flash occurs later, and after that flash a chime occurs.", "For every pulse, a flash occurs at the next step and a chime occurs at a later step."]}

### R019 / item_0007 (next_later)
A pulse must never be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R019", "comments": "", "interpretations": ["It is never the case that a pulse occurs and a flash occurs at any later step.", "No pulse is immediately followed by a flash.", "No flash occurs after any pulse; flashes may occur before pulses."]}

### R020 / item_0008 (next_later)
Every pulse must be followed by a flash before any subsequent stop, with no stop at the flash step.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R020", "comments": "", "interpretations": ["For every pulse, if a stop occurs afterward, a flash occurs after the pulse and before that stop, and the flash step is not a stop step.", "For every pulse, a flash occurs after it and before the next stop, with no stop at the flash step.", "For every pulse, a flash occurs before any later stop, and the flash and stop cannot coincide."]}

### R021 / item_0009 (next_later)
Every pair of pulses on consecutive steps must be followed by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R021", "comments": "", "interpretations": ["Whenever pulses occur at two consecutive steps, a flash occurs at some later step after the second pulse.", "Whenever pulses occur at two consecutive steps, a flash occurs at the next step after the pair.", "Whenever there are consecutive pulses, a flash occurs at some step after the first pulse."]}

### R022 / item_0010 (next_later)
Eventually, the rule that every pulse is followed by a flash must hold from then on.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R022", "comments": "", "interpretations": ["There is a future step from which every later pulse has a flash occurring later.", "There is a future step from which every pulse is immediately followed by a flash.", "Eventually the system enters a state where all pulses, whenever they occur, have a later flash."]}

### R023 / item_0011 (next_later)
A pulse followed by a flash must occur over and over without end.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R023", "comments": "", "interpretations": ["Infinitely often a pulse occurs and later a flash occurs.", "Infinitely often a pulse is immediately followed by a flash.", "From every point onward there is a future pulse-flash pair."]}

### R024 / item_0012 (next_later)
Once an activation occurs, every pulse from that step onward must be followed by a flash.
{"a": "an activation occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R024", "comments": "", "interpretations": ["After the first activation, every pulse at or after that step has a later flash.", "After any activation, every pulse from that activation step onward has a later flash.", "After activation, every pulse is immediately followed by a flash."]}

### R025 / item_0001 (same_later)
Requests require an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R025", "comments": "", "interpretations": ["At every step where a request occurs, the response is active at that same step.", "For every request, the response is active at some later step.", "For every request, the response is active at that step or later."]}

### R026 / item_0002 (same_later)
A request at the starting step requires an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R026", "comments": "", "interpretations": ["If a request occurs at the initial step, the response is active at that initial step.", "If a request occurs at the initial step, the response is active at some later step.", "If a request occurs at the initial step, the response is active at that step or later."]}

### R027 / item_0003 (same_later)
There must be a request with an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R027", "comments": "", "interpretations": ["At some future step a request occurs and the response is active at that same step.", "There exists a request and a response active at some possibly different step associated with it.", "At some future step a request occurs and the response is active at that step or later."]}

### R028 / item_0004 (same_later)
Requests with an active response must keep occurring.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R028", "comments": "", "interpretations": ["Infinitely often a request occurs while the response is active at the same step.", "From every point onward there is a future step with a request and an active response.", "Requests and active responses recur together infinitely often."]}

### R029 / item_0005 (same_later)
Eventually, requests must always have an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R029", "comments": "", "interpretations": ["There is a future step from which every request has the response active at the same step.", "There is a future step from which every request has the response active at some later step.", "Eventually, whenever a request occurs, the response is active at that step or later."]}

### R030 / item_0006 (same_later)
Requests require an active response until a release occurs, and a release must occur.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R030", "comments": "", "interpretations": ["Until the first release, every request has the response active at the same step; a release eventually occurs.", "Until a release, every request has the response active at that step or later; release is required.", "For every request before a release, the response is active at the request step; a release must occur."]}

### R031 / item_0007 (same_later)
Requests require an active response unless and until a release occurs.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R031", "comments": "", "interpretations": ["Before any release, every request has the response active at the same step; after release there is no requirement; release is optional.", "Until a release occurs, every request has the response active at that step or later; if no release occurs, the requirement holds forever.", "Requests require an active response until release, and release may never occur."]}

### R032 / item_0008 (same_later)
From the first release onward, requests require an active response.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R032", "comments": "", "interpretations": ["After the first release, every request has the response active at the same step.", "After the first release, every request has the response active at some later step.", "From the first release onward, whenever a request occurs, the response is active at that step or later."]}

### R033 / item_0009 (same_later)
Every request requires a response that remains active forever.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R033", "comments": "", "interpretations": ["For every request, from the request step onward the response is active forever.", "For every request, from some later step after the request the response is active forever.", "For every request, the response is active at the request step and stays active forever."]}

### R034 / item_0010 (same_later)
Every request requires the response to stay active until a release, which must occur.
{"a": "a request occurs", "b": "the response is active", "c": "a release occurs"}
{"review_id": "R034", "comments": "", "interpretations": ["For every request, the response stays active from the request step until a release occurs; a release eventually occurs.", "For every request, the response is active at the request step and remains active until some release; release is required.", "For every request, the response is active until the next release, and a release must occur."]}

### R035 / item_0011 (same_later)
A request at the next step requires an active response.
{"a": "a request occurs", "b": "the response is active"}
{"review_id": "R035", "comments": "", "interpretations": ["If a request occurs at the next step, the response is active at that next step.", "If a request occurs at the next step, the response is active at the step after that.", "If a request occurs at the next step, the response is active at that step or later."]}

### R036 / item_0012 (same_later)
Requests made while the response is permitted require an active response.
{"a": "a request occurs", "b": "the response is active", "c": "the response is permitted"}
{"review_id": "R036", "comments": "", "interpretations": ["At any step where a request occurs and the response is permitted, the response is active at that same step.", "At any step where a request occurs and the response is permitted, the response is active at some later step.", "At any step where a request and permission hold, the response is active at that step or later."]}

### R037 / item_0001 (trigger_scope_final)
A pulse is to be followed by a flash, possibly at the same step.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R037", "comments": "", "interpretations": ["For every pulse, a flash occurs at the same step or a later step.", "For every pulse, a flash occurs at some later step, not at the same step.", "For every pulse, a flash occurs at the next step or later."]}

### R038 / item_0002 (trigger_scope_final)
A pulse requires the light to be on at that step.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R038", "comments": "", "interpretations": ["At every step where a pulse occurs, the light is on at that same step.", "At every step where a pulse occurs, the light is on at that step or later.", "A pulse implies that the light is on at the pulse step."]}

### R039 / item_0003 (trigger_scope_final)
A pulse is to have a flash at the next step.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R039", "comments": "", "interpretations": ["For every pulse, a flash occurs at the immediately following step.", "For every pulse, a flash occurs at the next step or later.", "For every pulse, a flash occurs at the same step or the next step."]}

### R040 / item_0004 (trigger_scope_final)
A pulse requires the light to stay on from that step onward.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R040", "comments": "", "interpretations": ["For every pulse, from the pulse step onward the light is on forever.", "For every pulse, from the next step onward the light is on forever.", "After the first pulse, the light stays on forever."]}

### R041 / item_0005 (trigger_scope_final)
A pulse calls for the light to be on until a release occurs, with a release required.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R041", "comments": "", "interpretations": ["For every pulse, the light is on from the pulse step until a release occurs; a release eventually occurs.", "For every pulse, the light is on from the pulse step until the next release; release is required.", "For every pulse, the light stays on until some release, and a release must occur."]}

### R042 / item_0006 (trigger_scope_final)
A pulse calls for the light to stay on until a release, or forever if no release comes.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R042", "comments": "", "interpretations": ["For every pulse, the light is on from the pulse step until a release if one occurs; if no release occurs, the light stays on forever.", "For every pulse, the light is on until the next release; release is optional.", "For every pulse, the light remains on unless or until a release occurs."]}

### R043 / item_0007 (trigger_scope_final)
A pulse calls for the light to be on at the first release at or after that pulse, and that release must occur.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R043", "comments": "", "interpretations": ["For every pulse, there is a release at or after the pulse, and the light is on at that release step.", "For every pulse, the first release at or after it occurs and the light is on at that step.", "For every pulse, a release eventually occurs and the light is on at the first such release."]}

### R044 / item_0008 (trigger_scope_final)
A pulse calls for a release before any flash from that step onward, and a flash at or after the release.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a release occurs"}
{"review_id": "R044", "comments": "", "interpretations": ["For every pulse, from the pulse step onward a release occurs before any flash, and a flash occurs at or after that release.", "For every pulse, no flash occurs until a release occurs, and after the release a flash occurs.", "For every pulse, the next flash is preceded by a release, and a flash occurs at or after the release."]}

### R045 / item_0009 (trigger_scope_final)
A pulse while enabled calls for a flash at that step or later.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "an enable state holds"}
{"review_id": "R045", "comments": "", "interpretations": ["At any step where a pulse occurs and enable holds, a flash occurs at that same step or later.", "At any step where a pulse and enable hold, a flash occurs at some later step.", "At any step where a pulse and enable hold, a flash occurs at that step or the next step."]}

### R046 / item_0010 (trigger_scope_final)
Before the first stop, a pulse calls for a flash at that step or later.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R046", "comments": "", "interpretations": ["For every pulse before the first stop, a flash occurs at the pulse step or later, possibly after the stop.", "For every pulse before the first stop, a flash occurs at the pulse step or later but before the first stop.", "For every pulse before the first stop, a flash occurs at that step or later; a stop is not required."]}

### R047 / item_0001 (negation_scope)
The first and second indicators must not be active now.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R047", "comments": "", "interpretations": ["At the initial or current step, neither the first nor the second indicator is active.", "At the current step, it is not the case that both indicators are active; at least one is inactive.", "At the current step, both indicators are inactive."]}

### R048 / item_0002 (negation_scope)
The first and second indicators must never be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R048", "comments": "", "interpretations": ["At no step are both the first and second indicators active simultaneously.", "At no step is either the first or the second indicator active.", "Neither indicator is ever active; both are always inactive."]}

### R049 / item_0003 (negation_scope)
At some point, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R049", "comments": "", "interpretations": ["At some future step, neither indicator is active.", "At some future step, it is not the case that both indicators are active; at least one is inactive.", "At some future step, both indicators are inactive simultaneously."]}

### R050 / item_0004 (negation_scope)
Infinitely often, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R050", "comments": "", "interpretations": ["Infinitely often, neither indicator is active.", "Infinitely often, it is not the case that both indicators are active.", "Infinitely often, both indicators are inactive at the same step."]}

### R051 / item_0005 (negation_scope)
From some point onward, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active"}
{"review_id": "R051", "comments": "", "interpretations": ["There is a future step from which neither indicator is ever active.", "There is a future step from which it is never the case that both indicators are active.", "Eventually both indicators remain inactive forever."]}

### R052 / item_0006 (negation_scope)
The first and second indicators must not be active until a release occurs, and a release must occur.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a release occurs"}
{"review_id": "R052", "comments": "", "interpretations": ["Until the first release, neither indicator is active; a release eventually occurs.", "Until a release, it is not the case that both indicators are active; release is required.", "Before release both indicators are inactive, and a release must occur."]}

### R053 / item_0007 (negation_scope)
The first and second indicators must not be active until a release occurs; release is optional.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a release occurs"}
{"review_id": "R053", "comments": "", "interpretations": ["Until a release occurs, neither indicator is active; if no release occurs, they stay inactive forever.", "Until a release, it is not the case that both indicators are active; release is optional.", "Before any release both indicators are inactive; release may never occur."]}

### R054 / item_0008 (negation_scope)
Whenever the gate is open, the first and second indicators must not be active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "the gate is open"}
{"review_id": "R054", "comments": "", "interpretations": ["At every step where the gate is open, neither indicator is active.", "At every step where the gate is open, it is not the case that both indicators are active.", "While the gate is open, both indicators are inactive."]}

### R055 / item_0009 (negation_scope)
Whenever a pulse occurs, the first and second indicators must not be active at the immediately following step.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs"}
{"review_id": "R055", "comments": "", "interpretations": ["At the step immediately after any pulse, neither indicator is active.", "At the step immediately after any pulse, it is not the case that both indicators are active.", "At the next step after a pulse, both indicators are inactive."]}

### R056 / item_0010 (negation_scope)
Whenever a pulse occurs, there must be a step at that time or later when the first and second indicators are not active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs"}
{"review_id": "R056", "comments": "", "interpretations": ["For every pulse, at some step at or after the pulse, neither indicator is active.", "For every pulse, at some step at or after the pulse, it is not the case that both indicators are active.", "For every pulse, eventually after it both indicators are inactive."]}

### R057 / item_0011 (negation_scope)
Whenever a pulse occurs, the first and second indicators must not be active until a release occurs at that step or later, and such a release is required.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a pulse occurs", "d": "a release occurs"}
{"review_id": "R057", "comments": "", "interpretations": ["For every pulse, from the pulse step until a release at or after the pulse, neither indicator is active; a release eventually occurs.", "For every pulse, the indicators are not both active until a release at or after the pulse; release is required.", "For every pulse, both indicators are inactive until the next release at or after the pulse, and that release must occur."]}

### R058 / item_0012 (negation_scope)
A check must occur at a step when the first and second indicators are not active.
{"a": "the first indicator is active", "b": "the second indicator is active", "c": "a check occurs"}
{"review_id": "R058", "comments": "", "interpretations": ["At some future step, a check occurs and neither indicator is active at that same step.", "At some future step, a check occurs and it is not the case that both indicators are active.", "There is a check step where both indicators are inactive."]}

### R059 / item_0001 (or_scope)
Requests are answered by a pulse or a flash.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R059", "comments": "", "interpretations": ["For every request, a pulse or a flash occurs at some later step.", "For every request, a pulse or a flash occurs at the same step or later.", "For every request, either a pulse or a flash, or both, occurs at the next step."]}

### R060 / item_0002 (or_scope)
After a request, the next step must contain a pulse or a flash.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R060", "comments": "", "interpretations": ["For every request, at the immediately following step a pulse or a flash occurs.", "For every request, at the next step either a pulse or a flash, or both, occurs.", "For every request, the next step contains at least one of a pulse or a flash."]}

### R061 / item_0003 (or_scope)
A request must be answered at once by a pulse or a flash, but not both.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R061", "comments": "", "interpretations": ["For every request, at the next step exactly one of a pulse or a flash occurs.", "For every request, at the same step exactly one of a pulse or a flash occurs.", "For every request, immediately after it either a pulse or a flash occurs, but not both."]}

### R062 / item_0004 (or_scope)
Every request starts a pulse-then-flash or flash-then-pulse response, with the two events on consecutive steps.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs"}
{"review_id": "R062", "comments": "", "interpretations": ["For every request, either a pulse occurs and then a flash at the next step, or a flash occurs and then a pulse at the next step.", "For every request, the response begins at the next step with one event and the other event occurs at the following step.", "For every request, there is a consecutive pulse-flash pair or a consecutive flash-pulse pair after it."]}

### R063 / item_0005 (or_scope)
A request requires the first or second signal to stay active until a release, which must eventually occur.
{"a": "a request occurs", "b": "the first signal is active", "c": "the second signal is active", "d": "a release occurs"}
{"review_id": "R063", "comments": "", "interpretations": ["For every request, at least one of the first or second signal is active from the request step until a release; a release eventually occurs.", "For every request, either the first or second signal remains active until the next release; release is required.", "For every request, one of the signals stays active until some release, and a release must occur."]}

### R064 / item_0006 (or_scope)
A request requires the first or second signal to remain active unless released; release is optional.
{"a": "a request occurs", "b": "the first signal is active", "c": "the second signal is active", "d": "a release occurs"}
{"review_id": "R064", "comments": "", "interpretations": ["For every request, at least one signal stays active until a release if one occurs; if no release occurs, it stays active forever.", "For every request, one of the signals remains active unless or until release; release is optional.", "For every request, the first or second signal is active until release, and release may never occur."]}

### R065 / item_0007 (or_scope)
Until a stop occurs, requests must receive an immediate pulse or flash; a stop must eventually occur.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R065", "comments": "", "interpretations": ["Before the first stop, every request is followed at the next step by a pulse or a flash; a stop eventually occurs.", "Until a stop occurs, every request gets an immediate pulse or flash; a stop is required.", "Before any stop, requests are answered immediately, and a stop must occur."]}

### R066 / item_0008 (or_scope)
Unless a stop occurs, requests must receive an immediate pulse or flash; a stop is not required.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R066", "comments": "", "interpretations": ["If no stop ever occurs, every request is followed at the next step by a pulse or a flash; a stop is optional.", "Until a stop, if any, requests get an immediate pulse or flash; a stop is not required.", "Requests always get an immediate pulse or flash unless a stop occurs; a stop may never occur."]}

### R067 / item_0009 (or_scope)
Requests must receive a pulse or flash before the next stop.
{"a": "a request occurs", "b": "a pulse occurs", "c": "a flash occurs", "d": "a stop occurs"}
{"review_id": "R067", "comments": "", "interpretations": ["For every request, if a stop occurs afterward, a pulse or a flash occurs after the request and before that next stop.", "For every request, a pulse or a flash occurs before any subsequent stop; if no stop occurs, there is no requirement.", "For every request, a pulse or a flash occurs before the next stop."]}

### R068 / item_0001 (until_termination)
The state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R068", "comments": "", "interpretations": ["From now until the first release, the state is active; if no release occurs, the state stays active forever.", "The state remains active until a release occurs; release may or may not be required.", "The state is active at every step before a release."]}

### R069 / item_0002 (until_termination)
Whenever a request occurs, the state must remain active until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a request occurs"}
{"review_id": "R069", "comments": "", "interpretations": ["For every request, the state is active from the request step until a release occurs; if no release occurs, it stays active forever.", "For every request, the state is active until the next release; release is optional.", "For every request, the state remains active unless or until release."]}

### R070 / item_0003 (until_termination)
Eventually, the state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R070", "comments": "", "interpretations": ["There is a future step from which the state stays active until a release occurs; if no release occurs, it stays active forever.", "Eventually the state becomes active and remains active until a release; release is optional.", "At some future point the state is active until release."]}

### R071 / item_0004 (until_termination)
From every step onward, the state must stay active until a release occurs.
{"a": "the state is active", "b": "a release occurs"}
{"review_id": "R071", "comments": "", "interpretations": ["At every step, the state is active from that step until a release occurs; if no release occurs, it stays active forever.", "From any point, the state remains active until release; release is optional.", "The state is always active unless or until a release occurs."]}

### R072 / item_0005 (until_termination)
The state must remain active and the indicator lit until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "the indicator is lit"}
{"review_id": "R072", "comments": "", "interpretations": ["From now until a release, both the state is active and the indicator is lit; release is optional.", "Until release, the state is active and the indicator is lit; release may be required.", "Both conditions hold at every step before a release."]}

### R073 / item_0006 (until_termination)
The state must remain active until a release or a cancellation occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a cancellation occurs"}
{"review_id": "R073", "comments": "", "interpretations": ["The state is active until either a release or a cancellation occurs; if neither occurs, it stays active forever.", "The state is active until the first of release or cancellation; either event can end it.", "The state remains active unless or until release or cancellation."]}

### R074 / item_0007 (until_termination)
The state must remain active until a release occurs while the indicator is lit.
{"a": "the state is active", "b": "a release occurs", "c": "the indicator is lit"}
{"review_id": "R074", "comments": "", "interpretations": ["The state is active until a release, and at that release step the indicator is lit.", "The state is active until a release occurs, and the indicator is lit during that interval.", "The state is active until a release that occurs while the indicator is lit."]}

### R075 / item_0008 (until_termination)
The state must remain active until the indicator stays lit permanently.
{"a": "the state is active", "b": "the indicator is lit"}
{"review_id": "R075", "comments": "", "interpretations": ["The state is active until a point from which the indicator is lit forever; after that point there is no requirement.", "The state is active until the indicator becomes permanently lit; if that never happens, the state stays active forever.", "The state remains active until the indicator is permanently on."]}

### R076 / item_0009 (until_termination)
Whenever a request occurs, starting at the next step the state must remain active until a release occurs.
{"a": "the state is active", "b": "a release occurs", "c": "a request occurs"}
{"review_id": "R076", "comments": "", "interpretations": ["For every request, from the step after the request until a release, the state is active; release is optional.", "For every request, the state is active starting at the next step until release; if no release occurs, it stays active forever.", "For every request, from the next step onward the state is active until a release occurs."]}

### R077 / item_0010 (until_termination)
Until a release occurs, every pulse must be followed by a flash at the next step.
{"a": "a pulse occurs", "b": "a release occurs", "c": "a flash occurs"}
{"review_id": "R077", "comments": "", "interpretations": ["Before the first release, every pulse has a flash at the immediately following step.", "Until a release occurs, every pulse is followed by a flash at the next step; after release there is no requirement.", "Before any release, a pulse implies a flash at the next step."]}

### R078 / item_0011 (until_termination)
The first state must remain active until a handoff starts a second phase in which the second state remains active and a release must eventually end that phase.
{"a": "the first state is active", "b": "a handoff occurs", "c": "the second state is active", "d": "a release occurs"}
{"review_id": "R078", "comments": "", "interpretations": ["The first state is active until a handoff; after the handoff the second state is active until a release; a release eventually occurs.", "The first state is active until a handoff, then the second state is active until release; release is required to end the second phase.", "A handoff transitions from first state active to second state active, and a release eventually ends the second phase."]}

### R079 / item_0012 (until_termination)
A handoff must eventually occur with the first state active beforehand; from that handoff the second state must remain active until a release occurs.
{"a": "the first state is active", "b": "a handoff occurs", "c": "the second state is active", "d": "a release occurs"}
{"review_id": "R079", "comments": "", "interpretations": ["Eventually a handoff occurs while the first state is active; after it the second state is active until a release occurs.", "Eventually a handoff occurs with the first state active beforehand; from that handoff the second state is active until release, and release may be required.", "There is a future handoff preceded by the first state being active, then the second state is active until release."]}

### R080 / item_0001 (order_scope)
A pulse is to be followed later by a flash.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R080", "comments": "", "interpretations": ["For every pulse, a flash occurs at some strictly later step.", "For every pulse, a flash occurs at the next step or later.", "For every pulse, a flash occurs later, not at the same step."]}

### R081 / item_0002 (order_scope)
After a pulse, the light is to stay on from the next step onward.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R081", "comments": "", "interpretations": ["For every pulse, from the step after the pulse onward the light is on forever.", "For every pulse, from the next step onward the light stays on.", "After any pulse, the light is on permanently starting at the next step."]}

### R082 / item_0003 (order_scope)
After a pulse, the light is to settle into staying on at some later step.
{"a": "a pulse occurs", "b": "a light is on"}
{"review_id": "R082", "comments": "", "interpretations": ["For every pulse, there is a later step from which the light stays on forever.", "For every pulse, eventually after it the light becomes permanently on.", "After a pulse, at some future point the light stays on from then on."]}

### R083 / item_0004 (order_scope)
A pulse is to be followed later by a flash and, later still, a chime.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a chime occurs"}
{"review_id": "R083", "comments": "", "interpretations": ["For every pulse, a flash occurs later, and a chime occurs strictly later than that flash.", "For every pulse, a flash occurs later and a chime occurs later than the pulse, with the chime after the flash.", "For every pulse, the order is pulse, then flash, then chime."]}

### R084 / item_0005 (order_scope)
After a pulse, a flash is to occur later with no pulse in between.
{"a": "a pulse occurs", "b": "a flash occurs"}
{"review_id": "R084", "comments": "", "interpretations": ["For every pulse, there is a later flash such that no pulse occurs between that pulse and the flash.", "For every pulse, a flash occurs later and no pulse occurs strictly between the pulse and the flash.", "For every pulse, the flash occurs before any subsequent pulse."]}

### R085 / item_0006 (order_scope)
After a pulse, a flash is to occur later without a pause in between.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a pause state holds"}
{"review_id": "R085", "comments": "", "interpretations": ["For every pulse, a flash occurs later and the pause state does not hold between the pulse and the flash.", "For every pulse, a flash occurs at the next step, so there is no pause step in between.", "For every pulse, a flash occurs later with no intervening pause state."]}

### R086 / item_0007 (order_scope)
After a pulse, the next release is to occur with the light on.
{"a": "a pulse occurs", "b": "a light is on", "c": "a release occurs"}
{"review_id": "R086", "comments": "", "interpretations": ["For every pulse, at the first release after it, the light is on.", "For every pulse, the next release after it occurs and the light is on at that release.", "For every pulse, when the next release occurs, the light is on."]}

### R087 / item_0008 (order_scope)
A pulse while enabled is to be followed later by a flash.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "an enable state holds"}
{"review_id": "R087", "comments": "", "interpretations": ["At any step where a pulse occurs and enable holds, a flash occurs at some later step.", "At any step where a pulse and enable hold, a flash occurs at the next step or later.", "For every enabled pulse, a later flash occurs."]}

### R088 / item_0009 (order_scope)
Before the first stop, a pulse is to be followed later by a flash, also before that stop.
{"a": "a pulse occurs", "b": "a flash occurs", "c": "a stop occurs"}
{"review_id": "R088", "comments": "", "interpretations": ["For every pulse before the first stop, a flash occurs later than the pulse and before the first stop.", "For every pulse before the first stop, a flash occurs later and also before that stop.", "Before any stop, every pulse has a later flash before that stop."]}

## Stage 2

### R001
[{"reading_id": "a", "plain": "At least one step has both events."}, {"reading_id": "b", "plain": "Each event occurs at least once, possibly at different steps."}]
{"review_id": "R001", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R002
[{"reading_id": "a", "plain": "Both events coincide infinitely often."}, {"reading_id": "b", "plain": "Each event occurs infinitely often, without required coincidence."}]
{"review_id": "R002", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R003
[{"reading_id": "a", "plain": "Every request has a strictly later step with both events."}, {"reading_id": "b", "plain": "Every request has a strictly later pulse and a strictly later flash, possibly at different steps."}]
{"review_id": "R003", "comments": "", "additional_interpretations": ["Every request is followed by a pulse and then a flash, with the pulse before the flash."], "supports": {"a": "Not supported", "b": "Supported"}}

### R004
[{"reading_id": "a", "plain": "A joint occurrence is required before the first stop, if a stop occurs."}, {"reading_id": "b", "plain": "Each event is required before the first stop, at possibly different steps."}]
{"review_id": "R004", "comments": "", "additional_interpretations": ["A pulse occurs before a flash, both before the first stop."], "supports": {"a": "Not supported", "b": "Supported"}}

### R005
[{"reading_id": "a", "plain": "Starting strictly after each request, both events must coincide before any subsequent stop."}, {"reading_id": "b", "plain": "Starting strictly after each request, each event must occur before any subsequent stop, possibly separately."}]
{"review_id": "R005", "comments": "", "additional_interpretations": ["After each request, a pulse occurs before a flash, both before the next stop."], "supports": {"a": "Not supported", "b": "Supported"}}

### R006
[{"reading_id": "a", "plain": "Both states hold throughout the same pair of consecutive steps."}, {"reading_id": "b", "plain": "Each state has a pair of consecutive active steps, possibly different pairs."}]
{"review_id": "R006", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Not supported"}}

### R007
[{"reading_id": "a", "plain": "At some step both are inactive and at the next both are active."}, {"reading_id": "b", "plain": "Each independently changes from inactive to active at least once."}]
{"review_id": "R007", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R008
[{"reading_id": "a", "plain": "A common episode starts with both active and maintains both until a release occurs."}, {"reading_id": "b", "plain": "Each has its own active episode lasting until a release, possibly different episodes and releases."}]
{"review_id": "R008", "comments": "", "additional_interpretations": ["Both are active from some point until a release, or forever if no release occurs."], "supports": {"a": "Supported", "b": "Not supported"}}

### R009
[{"reading_id": "a", "plain": "A joint pulse-and-flash step occurs with a strictly later completion."}, {"reading_id": "b", "plain": "Each event occurs with some strictly later completion, possibly separately."}]
{"review_id": "R009", "comments": "", "additional_interpretations": ["A pulse occurs, then a flash, then a completion."], "supports": {"a": "Not supported", "b": "Supported"}}

### R010
[{"reading_id": "a", "plain": "Some start precedes a joint occurrence, which precedes a finish."}, {"reading_id": "b", "plain": "Some start precedes both events, which may occur separately before a finish."}]
{"review_id": "R010", "comments": "", "additional_interpretations": ["After a start, a pulse occurs before a flash, both before a finish."], "supports": {"a": "Not supported", "b": "Supported"}}

### R011
[{"reading_id": "a", "plain": "The two two-step sequences have the same starting step."}, {"reading_id": "b", "plain": "Each two-step sequence occurs, possibly starting at different steps."}]
{"review_id": "R011", "comments": "", "additional_interpretations": ["The pulse-flash and click-mark sequences occur in either order."], "supports": {"a": "Not supported", "b": "Supported"}}

### R012
[{"reading_id": "a", "plain": "There are infinitely many starting steps for a common two-step active episode."}, {"reading_id": "b", "plain": "Each has infinitely many two-step active episodes, with no required alignment."}]
{"review_id": "R012", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Not supported"}}

### R013
[{"reading_id": "a", "plain": "A flash occurs exactly one step after each pulse."}, {"reading_id": "b", "plain": "A flash occurs at some strictly later step after each pulse."}]
{"review_id": "R013", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R014
[{"reading_id": "a", "plain": "A pulse at the current step requires a flash at the next step."}, {"reading_id": "b", "plain": "A pulse at the current step requires a flash at some later step."}]
{"review_id": "R014", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R015
[{"reading_id": "a", "plain": "Some pulse has a flash at the next step."}, {"reading_id": "b", "plain": "Some pulse has a flash at a strictly later step."}]
{"review_id": "R015", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R016
[{"reading_id": "a", "plain": "The indicator is on at every step beginning at the next step after each pulse."}, {"reading_id": "b", "plain": "After each pulse, there is a later step from which the indicator is always on."}]
{"review_id": "R016", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Not supported"}}

### R017
[{"reading_id": "a", "plain": "The first stop eventually occurs, and every earlier pulse has a flash at its next step."}, {"reading_id": "b", "plain": "The first stop eventually occurs, and every earlier pulse has a flash at some strictly later step."}]
{"review_id": "R017", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R018
[{"reading_id": "a", "plain": "Each pulse has a flash at the next step, and a chime occurs later than that flash."}, {"reading_id": "b", "plain": "Each pulse has a flash at some later step, and a chime occurs still later."}]
{"review_id": "R018", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R019
[{"reading_id": "a", "plain": "No pulse has a flash at the next step."}, {"reading_id": "b", "plain": "No pulse has a flash at any strictly later step."}]
{"review_id": "R019", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R020
[{"reading_id": "a", "plain": "Each pulse has a flash without a stop at the next step."}, {"reading_id": "b", "plain": "Each pulse has a later flash, with no stop from the next step through that flash step."}]
{"review_id": "R020", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R021
[{"reading_id": "a", "plain": "Each consecutive pulse pair has a flash at the step immediately after its second pulse."}, {"reading_id": "b", "plain": "Each consecutive pulse pair has a flash at some strictly later step than its second pulse."}]
{"review_id": "R021", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R022
[{"reading_id": "a", "plain": "There is a step after which every pulse has a flash at the next step."}, {"reading_id": "b", "plain": "There is a step after which every pulse has a flash at some strictly later step."}]
{"review_id": "R022", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R023
[{"reading_id": "a", "plain": "Infinitely many pulses have a flash at the next step."}, {"reading_id": "b", "plain": "Infinitely many pulses have a flash at some strictly later step."}]
{"review_id": "R023", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R024
[{"reading_id": "a", "plain": "Beginning at the first activation step, every pulse has a flash at the next step."}, {"reading_id": "b", "plain": "Beginning at the first activation step, every pulse has a flash at some strictly later step."}]
{"review_id": "R024", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R025
[{"reading_id": "a", "plain": "Every request has an active response at its own step."}, {"reading_id": "b", "plain": "Every request has an active response at some strictly later step."}]
{"review_id": "R025", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R026
[{"reading_id": "a", "plain": "A starting-step request requires the response at the starting step."}, {"reading_id": "b", "plain": "A starting-step request requires the response strictly later."}]
{"review_id": "R026", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R027
[{"reading_id": "a", "plain": "Some request coincides with an active response."}, {"reading_id": "b", "plain": "Some request has an active response strictly later."}]
{"review_id": "R027", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Not supported"}}

### R028
[{"reading_id": "a", "plain": "Infinitely many requests coincide with an active response."}, {"reading_id": "b", "plain": "Infinitely many requests have an active response strictly later."}]
{"review_id": "R028", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Not supported"}}

### R029
[{"reading_id": "a", "plain": "From some point onward, each request coincides with an active response."}, {"reading_id": "b", "plain": "From some point onward, each request has an active response strictly later."}]
{"review_id": "R029", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R030
[{"reading_id": "a", "plain": "Before the first release, every request coincides with an active response; a release occurs."}, {"reading_id": "b", "plain": "Before the first release, every request has an active response strictly later; a release occurs."}]
{"review_id": "R030", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R031
[{"reading_id": "a", "plain": "Every request before the first release, or forever if no release occurs, coincides with an active response."}, {"reading_id": "b", "plain": "Every request before the first release, or forever if no release occurs, has an active response strictly later."}]
{"review_id": "R031", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R032
[{"reading_id": "a", "plain": "At and after the first release, every request coincides with an active response."}, {"reading_id": "b", "plain": "At and after the first release, every request has an active response strictly later."}]
{"review_id": "R032", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R033
[{"reading_id": "a", "plain": "For each request, the response is active from the request step forever."}, {"reading_id": "b", "plain": "For each request, the response is active forever starting at some strictly later step."}]
{"review_id": "R033", "comments": "Both immediate and delayed start of permanent activity are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R034
[{"reading_id": "a", "plain": "Each request starts a requirement for activity at that step and until a release occurs."}, {"reading_id": "b", "plain": "Each request has a strictly later step starting a requirement for activity then and until a release occurs."}]
{"review_id": "R034", "comments": "", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Not supported"}}

### R035
[{"reading_id": "a", "plain": "A request exactly one step from the start requires a response at that same step."}, {"reading_id": "b", "plain": "A request exactly one step from the start requires a response at some step after it."}]
{"review_id": "R035", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R036
[{"reading_id": "a", "plain": "Every request made when permission holds coincides with an active response."}, {"reading_id": "b", "plain": "Every request made when permission holds has an active response strictly later."}]
{"review_id": "R036", "comments": "Both same-step and later-response readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R037
[{"reading_id": "a", "plain": "At least one qualifying pulse has a flash at that step or some later step."}, {"reading_id": "b", "plain": "Every qualifying pulse has a flash at that step or some later step; no pulse is required."}]
{"review_id": "R037", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R038
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on at its step."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on at its step; no pulse is required."}]
{"review_id": "R038", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R039
[{"reading_id": "a", "plain": "At least one qualifying pulse has a flash exactly one step afterward."}, {"reading_id": "b", "plain": "Every qualifying pulse has a flash exactly one step afterward; no pulse is required."}]
{"review_id": "R039", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R040
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on at that step and every subsequent step."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on at that step and every subsequent step; no pulse is required."}]
{"review_id": "R040", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R041
[{"reading_id": "a", "plain": "At least one qualifying pulse has a release at or after its step and the light on at every step from the pulse up to but excluding that release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a release at or after its step and the light on at every step from the pulse up to but excluding that release; no pulse is required."}]
{"review_id": "R041", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R042
[{"reading_id": "a", "plain": "At least one qualifying pulse has the light on from its step until just before a release, or forever if there is no release."}, {"reading_id": "b", "plain": "Every qualifying pulse has the light on from its step until just before a release, or forever if there is no release; no pulse is required."}]
{"review_id": "R042", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R043
[{"reading_id": "a", "plain": "At least one qualifying pulse has a first release at or after its step, with the light on at that release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a first release at or after its step, with the light on at that release; no pulse is required."}]
{"review_id": "R043", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R044
[{"reading_id": "a", "plain": "At least one qualifying pulse has a release at or after its step, no flashes before that release from the pulse onward, and a flash at or after the release."}, {"reading_id": "b", "plain": "Every qualifying pulse has a release at or after its step, no flashes before that release from the pulse onward, and a flash at or after the release; no pulse is required."}]
{"review_id": "R044", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R045
[{"reading_id": "a", "plain": "At least one qualifying pulse occurs while enabled and has a flash at that step or later."}, {"reading_id": "b", "plain": "Every qualifying pulse occurs while enabled and has a flash at that step or later; no pulse is required."}]
{"review_id": "R045", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R046
[{"reading_id": "a", "plain": "At least one qualifying pulse occurs strictly before the first stop, if any, and has a flash at its step or later."}, {"reading_id": "b", "plain": "Every qualifying pulse occurs strictly before the first stop, if any, and has a flash at its step or later; no pulse is required."}]
{"review_id": "R046", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R047
[{"reading_id": "a", "plain": "At the current step, at least one indicator is inactive."}, {"reading_id": "b", "plain": "At the current step, each indicator is inactive."}]
{"review_id": "R047", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R048
[{"reading_id": "a", "plain": "At every step, at least one indicator is inactive."}, {"reading_id": "b", "plain": "At every step, each indicator is inactive."}]
{"review_id": "R048", "comments": "Both 'never both active' and 'neither ever active' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R049
[{"reading_id": "a", "plain": "Some step has at least one inactive indicator."}, {"reading_id": "b", "plain": "Some step has each indicator inactive."}]
{"review_id": "R049", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R050
[{"reading_id": "a", "plain": "Infinitely many steps have at least one inactive indicator."}, {"reading_id": "b", "plain": "Infinitely many steps have each indicator inactive."}]
{"review_id": "R050", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R051
[{"reading_id": "a", "plain": "Eventually every remaining step has at least one inactive indicator, with the inactive indicator allowed to vary."}, {"reading_id": "b", "plain": "Eventually each indicator stays inactive forever."}]
{"review_id": "R051", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R052
[{"reading_id": "a", "plain": "A release eventually occurs; at each earlier step at least one indicator is inactive."}, {"reading_id": "b", "plain": "A release eventually occurs; at each earlier step each indicator is inactive."}]
{"review_id": "R052", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R053
[{"reading_id": "a", "plain": "Before the first release, at least one indicator is inactive at every step; if no release occurs this lasts forever."}, {"reading_id": "b", "plain": "Before the first release, each indicator is inactive at every step; if no release occurs this lasts forever."}]
{"review_id": "R053", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R054
[{"reading_id": "a", "plain": "Every open-gate step has at least one inactive indicator."}, {"reading_id": "b", "plain": "Every open-gate step has each indicator inactive."}]
{"review_id": "R054", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R055
[{"reading_id": "a", "plain": "The step immediately after every pulse has at least one inactive indicator."}, {"reading_id": "b", "plain": "The step immediately after every pulse has each indicator inactive."}]
{"review_id": "R055", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R056
[{"reading_id": "a", "plain": "Every pulse has a current or later step with at least one inactive indicator."}, {"reading_id": "b", "plain": "Every pulse has a current or later step with each indicator inactive."}]
{"review_id": "R056", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R057
[{"reading_id": "a", "plain": "Each pulse requires a current or later release, with at least one indicator inactive at every step from the pulse up to but excluding that release."}, {"reading_id": "b", "plain": "Each pulse requires a current or later release, with each indicator inactive at every step from the pulse up to but excluding that release."}]
{"review_id": "R057", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R058
[{"reading_id": "a", "plain": "Some check occurs with at least one indicator inactive."}, {"reading_id": "b", "plain": "Some check occurs with each indicator inactive."}]
{"review_id": "R058", "comments": "Both 'not both active' and 'both inactive' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R059
[{"reading_id": "a", "plain": "One response type answers every request at its own step."}, {"reading_id": "b", "plain": "Each request has a response at its own step, with the type allowed to vary."}]
{"review_id": "R059", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R060
[{"reading_id": "a", "plain": "One response type is required at the step immediately after every request."}, {"reading_id": "b", "plain": "The step immediately after each request has either response type, with the type allowed to vary."}]
{"review_id": "R060", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R061
[{"reading_id": "a", "plain": "The same sole response type occurs at every request step."}, {"reading_id": "b", "plain": "Exactly one response occurs at each request step, and the chosen type can change."}]
{"review_id": "R061", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R062
[{"reading_id": "a", "plain": "One event ordering applies to every request, starting at its step."}, {"reading_id": "b", "plain": "Each request begins either ordering, and the ordering can vary."}]
{"review_id": "R062", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R063
[{"reading_id": "a", "plain": "One signal is required from each request until a release; every request must reach a release."}, {"reading_id": "b", "plain": "Each request chooses a signal to maintain until a release, and every request must reach a release."}]
{"review_id": "R063", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R064
[{"reading_id": "a", "plain": "One signal serves all requests and stays active until release, or forever if no release occurs."}, {"reading_id": "b", "plain": "A signal is chosen per request and maintained until release, or forever without release."}]
{"review_id": "R064", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R065
[{"reading_id": "a", "plain": "Before a required stop, one response type answers all requests at their own steps."}, {"reading_id": "b", "plain": "Before a required stop, requests receive same-step responses whose types can vary."}]
{"review_id": "R065", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R066
[{"reading_id": "a", "plain": "One response type answers all requests before the first stop, or forever if there is no stop."}, {"reading_id": "b", "plain": "Response types may vary among requests before the first stop, or forever without a stop."}]
{"review_id": "R066", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R067
[{"reading_id": "a", "plain": "One response type must occur for every request before any stop at or after that request."}, {"reading_id": "b", "plain": "Each request must get either response type before a stop, with types allowed to vary."}]
{"review_id": "R067", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R068
[{"reading_id": "a", "plain": "A release eventually occurs, and the state is active at every earlier step."}, {"reading_id": "b", "plain": "The state stays active before a release; if no release occurs, it stays active forever."}]
{"review_id": "R068", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R069
[{"reading_id": "a", "plain": "Every request has a release at that step or later, with activity at each intervening step."}, {"reading_id": "b", "plain": "Every request requires activity before a release, or forever if none follows."}]
{"review_id": "R069", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R070
[{"reading_id": "a", "plain": "Some step starts an activity interval ending in a release, possibly immediately."}, {"reading_id": "b", "plain": "Some step starts an activity interval ending in a release or continuing forever."}]
{"review_id": "R070", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R071
[{"reading_id": "a", "plain": "At each step a release is still forthcoming, and activity holds before it."}, {"reading_id": "b", "plain": "At each step activity holds before the next release, and forever if releases stop."}]
{"review_id": "R071", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R072
[{"reading_id": "a", "plain": "Both maintained conditions hold before an eventual release."}, {"reading_id": "b", "plain": "Both maintained conditions hold before a release, or forever without one."}]
{"review_id": "R072", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R073
[{"reading_id": "a", "plain": "At least one terminating event eventually occurs, with prior activity."}, {"reading_id": "b", "plain": "Activity persists until either terminating event, or forever if neither occurs."}]
{"review_id": "R073", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R074
[{"reading_id": "a", "plain": "A release with a lit indicator eventually occurs, with activity before that joint condition."}, {"reading_id": "b", "plain": "Activity lasts until a release with a lit indicator, or forever if that combination never occurs."}]
{"review_id": "R074", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R075
[{"reading_id": "a", "plain": "The indicator eventually becomes permanently lit, with activity before a qualifying start."}, {"reading_id": "b", "plain": "Activity continues until permanent illumination starts, or forever if it never does."}]
{"review_id": "R075", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R076
[{"reading_id": "a", "plain": "Every request initiates a next-step interval that must end in a release."}, {"reading_id": "b", "plain": "Every request initiates a next-step interval that may persist without release."}]
{"review_id": "R076", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R077
[{"reading_id": "a", "plain": "A release eventually occurs; pulses before it require next-step flashes."}, {"reading_id": "b", "plain": "Pulses before a release require next-step flashes; without a release this rule applies forever."}]
{"review_id": "R077", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R078
[{"reading_id": "a", "plain": "A qualifying handoff eventually occurs and begins a second phase with mandatory release."}, {"reading_id": "b", "plain": "A qualifying handoff may never occur if the first state remains active forever; if it occurs the second phase has mandatory release."}]
{"review_id": "R078", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R079
[{"reading_id": "a", "plain": "A handoff and then a release occur, with the corresponding state active before each endpoint."}, {"reading_id": "b", "plain": "A handoff occurs, after which the second state may remain active forever without release."}]
{"review_id": "R079", "comments": "Both strong and weak 'until' readings are plausible.", "additional_interpretations": [], "supports": {"a": "Supported", "b": "Supported"}}

### R080
[{"reading_id": "a", "plain": "At least one pulse must occur with a flash at a strictly later step."}, {"reading_id": "b", "plain": "Every pulse must have a flash at a strictly later step; pulses need not occur."}]
{"review_id": "R080", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R081
[{"reading_id": "a", "plain": "At least one pulse must occur after which the light is on at every step starting with the next step."}, {"reading_id": "b", "plain": "After every pulse, the light must be on at every step starting with the next step; pulses need not occur."}]
{"review_id": "R081", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R082
[{"reading_id": "a", "plain": "At least one pulse must occur, and at some strictly later step the light must begin remaining on forever."}, {"reading_id": "b", "plain": "For every pulse, there must be a strictly later step from which the light stays on forever; pulses need not occur."}]
{"review_id": "R082", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R083
[{"reading_id": "a", "plain": "At least one pulse must occur with a later flash and a chime strictly later than that flash."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash and a chime strictly later than that flash; pulses need not occur."}]
{"review_id": "R083", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R084
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later flash and no pulse strictly between them; a pulse at the flash step is allowed."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash with no pulse strictly between them; a pulse at the flash step is allowed, and pulses need not occur."}]
{"review_id": "R084", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R085
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later flash and no pause state strictly between them; pause states at the endpoints are allowed."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later flash with no pause state strictly between them; pause states at the endpoints are allowed, and pulses need not occur."}]
{"review_id": "R085", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R086
[{"reading_id": "a", "plain": "At least one pulse must occur with a strictly later release, and the light must be on at the first release strictly after that pulse."}, {"reading_id": "b", "plain": "Every pulse must have a strictly later release, and the light must be on at the first release strictly after it; pulses need not occur."}]
{"review_id": "R086", "comments": "", "additional_interpretations": ["For every pulse, if a later release occurs, the light is on at the first such release."], "supports": {"a": "Not supported", "b": "Supported"}}

### R087
[{"reading_id": "a", "plain": "At least one pulse must occur while enabled and have a strictly later flash; the enable state need not persist."}, {"reading_id": "b", "plain": "Every pulse occurring while enabled must have a strictly later flash; the enable state need not persist and enabled pulses need not occur."}]
{"review_id": "R087", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}

### R088
[{"reading_id": "a", "plain": "At least one pulse must occur and have a strictly later flash, both before the first stop; if no stop occurs both events must still occur."}, {"reading_id": "b", "plain": "Every pulse before the first stop must have a strictly later flash before that stop; if no stop occurs apply this rule forever, and pulses need not occur."}]
{"review_id": "R088", "comments": "", "additional_interpretations": [], "supports": {"a": "Not supported", "b": "Supported"}}
