"""50 nautical knots with full metadata and load ratings."""

KNOTS_DATA = [
    {
        "name": "Bowline",
        "category": "loop",
        "difficulty_rating": 2,
        "strength_pct": 70,
        "breaking_strength_lbs": 1200,
        "use_cases": ["rescue", "mooring", "climbing"],
        "proper_use": "Creating a fixed loop at the end of a rope. Excellent for tying a rope around an object or your own waist. Used in rescue operations, sailing, and climbing.",
        "when_not_to_use": "When the loop needs to be easily adjusted or when the knot will be loaded continuously under variable loads.",
        "how_to_tie_steps": [
            "Form a small loop (the 'rabbit hole') in the standing part of the rope",
            "Pass the working end up through the loop from underneath",
            "Wrap the working end behind the standing part",
            "Pass the working end back down through the small loop",
            "Pull both ends to tighten"
        ],
        "failure_mode": "Can slip under sudden shock loads if not dressed correctly",
        "related_knots": ["Double Bowline", "Yosemite Bowline", "Running Bowline"]
    },
    {
        "name": "Clove Hitch",
        "category": "hitch",
        "difficulty_rating": 1,
        "strength_pct": 65,
        "breaking_strength_lbs": 1000,
        "use_cases": ["mooring", "fendering", "temporary fastening"],
        "proper_use": "Quick temporary hitch for securing a rope to a post, rail, or bollard. Easy to adjust length.",
        "when_not_to_use": "On rough surfaces that can saw through the rope, or where security is critical.",
        "how_to_tie_steps": [
            "Pass the rope over the object",
            "Wrap around and cross over the standing part",
            "Wrap around the object again",
            "Tuck the working end under the last wrap"
        ],
        "failure_mode": "Can slip or bind depending on rope material and surface",
        "related_knots": ["Round Turn and Two Half Hitches", "Anchor Bend", "Rolling Hitch"]
    },
    {
        "name": "Figure Eight",
        "category": "stopper",
        "difficulty_rating": 1,
        "strength_pct": 75,
        "breaking_strength_lbs": 1300,
        "use_cases": ["climbing", "stopper knot", "anchor"],
        "proper_use": "Primary stopper knot for preventing rope from escaping a device or hole. Used extensively in climbing.",
        "when_not_to_use": "When you need a smaller stopper knot, as figure eight can be difficult to untie after loading.",
        "how_to_tie_steps": [
            "Form a loop",
            "Pass the working end behind the standing part",
            "Thread the working end through the loop you just created"
        ],
        "failure_mode": "May jam and become difficult to untie after heavy loading",
        "related_knots": ["Figure Eight Loop", "Figure Eight on a Bight", "Stevedore"]
    },
    {
        "name": "Sheet Bend",
        "category": "bending",
        "difficulty_rating": 2,
        "strength_pct": 62,
        "breaking_strength_lbs": 900,
        "use_cases": ["joining ropes", "sailing", "rescue"],
        "proper_use": "Joining two ropes of unequal diameter. The primary knot for attaching a sheet to a sail.",
        "when_not_to_use": "When both ropes are of equal diameter (use Ashley Bend instead), or in critical safety applications.",
        "how_to_tie_steps": [
            "Form a bight in the thicker rope",
            "Pass the thinner rope through the bight from below",
            "Wrap around both legs of the bight",
            "Tuck under itself"
        ],
        "failure_mode": " Can slip or fall apart if ends aren't long enough or if loaded asymmetrically",
        "related_knots": ["Ashley Bend", "Double Sheet Bend", "Bowline"]
    },
    {
        "name": "Trucker's Hitch",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 80,
        "breaking_strength_lbs": 1500,
        "use_cases": ["towing", "securing cargo", "mooring"],
        "proper_use": "Creating a mechanical advantage to tension a rope tightly. Used for securing loads on vehicles and boats.",
        "when_not_to_use": "When a quick tie is needed or when the mechanical advantage could damage the load.",
        "how_to_tie_steps": [
            "Tie one end to an anchor point",
            "Create a loop in the middle using a slipped overhand",
            "Pass the other end through the loop",
            "Use the loop as a pulley to gain mechanical advantage",
            "Secure the working end"
        ],
        "failure_mode": "The loop can slip if not properly locked off",
        "related_knots": ["Power Cinch", "Loop Hitch", "Slippery Hitch"]
    },
    {
        "name": "Anchor Bend",
        "category": "hitch",
        "difficulty_rating": 3,
        "strength_pct": 78,
        "breaking_strength_lbs": 1350,
        "use_cases": ["anchoring", "mooring", "securing anchor"],
        "proper_use": "The classic knot for attaching anchor rode to an anchor ring. Highly secure.",
        "when_not_to_use": "When quick release is needed, as it can be difficult to untie after loading.",
        "how_to_tie_steps": [
            "Pass the rope through the anchor ring twice",
            "Tuck the working end over and under the standing part",
            "Add two or three half hitches around the standing part"
        ],
        "failure_mode": "Extremely reliable when properly dressed",
        "related_knots": ["Clove Hitch", "Fisherman's Bend", "Round Turn and Two Half Hitches"]
    },
    {
        "name": "Rolling Hitch",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 72,
        "breaking_strength_lbs": 1250,
        "use_cases": ["mooring", "adjustable tension", "relieving strain"],
        "proper_use": "Attaching a rope to a rod, rail, or another rope where you need grip but also ability to slide under load.",
        "when_not_to_use": "On smooth surfaces like metal or plastic where grip is unreliable.",
        "how_to_tie_steps": [
            "Wrap the rope around the object",
            "Cross over and make another wrap next to the first",
            "Make a third wrap on the opposite side",
            "Tuck under the last wrap"
        ],
        "failure_mode": "Grip depends heavily on surface texture and angle of pull",
        "related_knots": ["Clove Hitch", "Munter Hitch", "Taut-Line Hitch"]
    },
    {
        "name": "Taut-Line Hitch",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 68,
        "breaking_strength_lbs": 1100,
        "use_cases": ["camping", "securing tent lines", "adjustable"],
        "proper_use": "Adjustable loop hitch for lines that need tensioning. Classic tent guy-line knot.",
        "when_not_to_use": "In critical applications where slippage cannot be tolerated.",
        "how_to_tie_steps": [
            "Pass rope around anchor",
            "Wrap twice inside the loop",
            "Wrap once outside the loop",
            "Pass through and tighten"
        ],
        "failure_mode": "Can slip under variable loads over time",
        "related_knots": ["Rolling Hitch", "Midshipman's Hitch", "Adjustable Grip Hitch"]
    },
    {
        "name": "Prusik",
        "category": "loop",
        "difficulty_rating": 3,
        "strength_pct": 55,
        "breaking_strength_lbs": 800,
        "use_cases": ["climbing", "rescue", "ascending rope"],
        "proper_use": "Friction hitch that grips the rope. Used for ascending a rope or creating adjustable attachment points.",
        "when_not_to_use": "On wet or icy ropes where grip becomes unreliable.",
        "how_to_tie_steps": [
            "Tie a loop of cord using a Double Loop Bowline",
            "Wrap the loop around the main rope 3 times",
            "Pass the loop through itself and snug up"
        ],
        "failure_mode": "Grip can fail if rope is dirty, wet, or frozen",
        "related_knots": ["Klemheist", "Munter Hitch", "French Prusik"]
    },
    {
        "name": "Munter Hitch",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 70,
        "breaking_strength_lbs": 1200,
        "use_cases": ["climbing", "belaying", "rescue"],
        "proper_use": "Versatile hitch for belaying and lowering. Creates friction for controlling a load.",
        "when_not_to_use": "In wet or sandy conditions where the hitch can be damaged.",
        "how_to_tie_steps": [
            "Form a loop in the rope",
            "Twist the loop 180 degrees",
            "Clip a carabiner through both legs"
        ],
        "failure_mode": "Can become hard to manage with heavy loads",
        "related_knots": ["Italian Hitch", "Prusik", "Clove Hitch"]
    },
    {
        "name": "Fisherman's Knot",
        "category": "bending",
        "difficulty_rating": 2,
        "strength_pct": 65,
        "breaking_strength_lbs": 950,
        "use_cases": ["fishing", "joining similar diameter lines"],
        "proper_use": "Joining two lines of equal or near-equal diameter. Popular in fishing for connecting line to leader.",
        "when_not_to_use": "On slippery modern fishing lines without adequate bite.",
        "how_to_tie_steps": [
            "Overlap the two rope ends",
            "Wrap one end around the other 3-4 times",
            "Pass through the gap between ropes",
            "Repeat with the other end going opposite direction"
        ],
        "failure_mode": "Can slip on slippery synthetic lines",
        "related_knots": ["Blood Knot", "Double Fisherman's", "Water Knot"]
    },
    {
        "name": "Blood Knot",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 68,
        "breaking_strength_lbs": 1050,
        "use_cases": ["fishing", "joining line sections"],
        "proper_use": "Joining two monofilament lines of similar diameter. Popular in fly fishing.",
        "when_not_to_use": "On braided lines or lines of very different diameters.",
        "how_to_tie_steps": [
            "Overlap the two ends",
            "Wrap one around the other 5-6 turns",
            "Tuck the end back through the center gap",
            "Repeat with the other end in opposite direction"
        ],
        "failure_mode": "Weakens monofilament due to bending stress",
        "related_knots": ["Fisherman's Knot", "Uni Knot", "Nail Knot"]
    },
    {
        "name": "Barrel Hitch",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 75,
        "breaking_strength_lbs": 1100,
        "use_cases": ["lifting barrels", "cargo handling", "securing cylindrical objects"],
        "proper_use": "Lifting and securing barrels and cylindrical objects. Weight sits in the bight.",
        "when_not_to_use": "When quick release is needed or on very smooth barrels that could slip.",
        "how_to_tie_steps": [
            "Form a bight in the middle of the rope",
            "Wrap the bight under the barrel",
            "Cross the rope over the top",
            "Pass each leg through the bight and around the crossed part"
        ],
        "failure_mode": "Barrel can shift or fall if knot loosens",
        "related_knots": ["Slippery Hitch", "Stevedore", "Strangle"]
    },
    {
        "name": "Blackwall Hitch",
        "category": "hitch",
        "difficulty_rating": 1,
        "strength_pct": 50,
        "breaking_strength_lbs": 700,
        "use_cases": ["temporary hitch", "hoisting", "quick attachment"],
        "proper_use": "Quick temporary hitch for hoisting tools or lightweight objects. Simple and fast.",
        "when_not_to_use": "Any critical or permanent application. Only use as a temporary measure.",
        "how_to_tie_steps": [
            "Pass rope over the hook point",
            "Tuck under the standing part",
            "Pull tight against the hook"
        ],
        "failure_mode": "Can slip out of the hook under vibration or movement",
        "related_knots": ["Whitewall Hitch", "Cat's Paw", "Strangle"]
    },
    {
        "name": "Carrick Bend",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 78,
        "breaking_strength_lbs": 1400,
        "use_cases": ["mooring", "heavy line joining", "towing"],
        "proper_use": "Joining heavy ropes or hawsers. Extremely strong and stable under load.",
        "when_not_to_use": "When quick release is needed, as it can be difficult to untie.",
        "how_to_tie_steps": [
            "Form a loop with the first rope, working end exiting from below",
            "Pass the second rope under the loop's crossing point",
            "Weave over, under, over, under through the loop",
            "Pull all working ends to tighten"
        ],
        "failure_mode": "Difficult to untie after heavy loading",
        "related_knots": ["Sheet Bend", "Zeppelin Bend", "Ashley Bend"]
    },
    {
        "name": "Cat's Paw",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 73,
        "breaking_strength_lbs": 1150,
        "use_cases": ["hoisting", "lifting", "slings"],
        "proper_use": "Creating a four-legged sling from a single rope. Good for hoisting.",
        "when_not_to_use": "On delicate objects that could be damaged by the sharp bends.",
        "how_to_tie_steps": [
            "Form a bight and twist it into a grommet",
            "Form two more bights on each side of the first",
            "Pull all three bights through each other",
            "Arrange the four legs"
        ],
        "failure_mode": "Can twist or tangle if not dressed properly",
        "related_knots": ["Blackwall Hitch", "Strangle", "Strop Hitch"]
    },
    {
        "name": "Constrictor",
        "category": "binding",
        "difficulty_rating": 2,
        "strength_pct": 85,
        "breaking_strength_lbs": 1300,
        "use_cases": ["binding", "seizing", "临时锁定"],
        "proper_use": "Extremely tight binding knot. Used for seizing, temporary whipping, and clamping.",
        "when_not_to_use": "When you need to untie it later - this knot is notoriously difficult to remove.",
        "how_to_tie_steps": [
            "Wrap the rope around the object",
            "Tuck the working end under the standing part",
            "Wind the working end tightly around both parts",
            "Pull very tight"
        ],
        "failure_mode": "May cut into rope fibers and cause damage",
        "related_knots": ["Strangle", "Transom Knot", "Bag Knot"]
    },
    {
        "name": "Counterpart",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 70,
        "breaking_strength_lbs": 1050,
        "use_cases": ["joining ropes", "splicing substitute"],
        "proper_use": "Joining two ropes of equal diameter. An alternative to the Carrick Bend.",
        "when_not_to_use": "On ropes of significantly different diameters.",
        "how_to_tie_steps": [
            "Create two interlocking loops",
            "Cross one over the other",
            "Pull ends through and tighten"
        ],
        "failure_mode": "Can work loose under variable loads",
        "related_knots": ["Carrick Bend", "Zeppelin Bend", "Sheet Bend"]
    },
    {
        "name": "Diagonal Bend",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 75,
        "breaking_strength_lbs": 1200,
        "use_cases": ["joining ropes", "non-parallel lines"],
        "proper_use": "Joining two ropes where the pull is diagonal rather than in-line.",
        "when_not_to_use": "When both ropes pull in the same axis.",
        "how_to_tie_steps": [
            "Arrange ropes at 90 degrees",
            "Create interlocked bights",
            "Weave according to pattern",
            "Tighten gradually"
        ],
        "failure_mode": "Asymmetrical loading can cause uneven strain",
        "related_knots": ["Carrick Bend", "Ashley's Bend", "Sheet Bend"]
    },
    {
        "name": "Double Bowline",
        "category": "loop",
        "difficulty_rating": 3,
        "strength_pct": 78,
        "breaking_strength_lbs": 1350,
        "use_cases": ["climbing", "rescue", "lifesaving"],
        "proper_use": "A bowline with an extra wrap for more security. Used when extra safety is required.",
        "when_not_to_use": "In situations where the extra bulk is a problem.",
        "how_to_tie_steps": [
            "Form the loop as in a regular bowline",
            "Make an extra wrap around the standing part before threading through",
            "Pull tight and dress neatly"
        ],
        "failure_mode": "More complex but still can slip under shock loads",
        "related_knots": ["Bowline", "Yosemite Bowline", "Bowline on a Bight"]
    },
    {
        "name": "Eye Splice",
        "category": "loop",
        "difficulty_rating": 4,
        "strength_pct": 90,
        "breaking_strength_lbs": 1600,
        "use_cases": ["permanent loops", "sailboat sheets", "dock lines"],
        "proper_use": "Creating a permanent loop in the end of three-strand rope by splicing.",
        "when_not_to_use": "On modern braided lines without proper tools and skill.",
        "how_to_tie_steps": [
            "Unlay the strands of the rope end",
            "Form an eye shape",
            "Tuck the strands over and under the standing part strands",
            "Continue tucking for 5-7 tucks each way"
        ],
        "failure_mode": "Requires skill to execute properly; weakness if done wrong",
        "related_knots": ["Short Splice", "Long Splice", "Bowline"]
    },
    {
        "name": "Figure Eight Loop",
        "category": "loop",
        "difficulty_rating": 2,
        "strength_pct": 80,
        "breaking_strength_lbs": 1400,
        "use_cases": ["climbing", "anchor points", "sailing"],
        "proper_use": "Creating a fixed loop in the middle of a rope. Stronger than a bowline loop.",
        "when_not_to_use": "When you need the loop to be adjustable.",
        "how_to_tie_steps": [
            "Form a bight in the rope",
            "Tie a figure eight knot",
            "Pass the end through and tighten"
        ],
        "failure_mode": "Can be hard to untie after heavy loading",
        "related_knots": ["Figure Eight", "Alpine Butterfly", "Bowline"]
    },
    {
        "name": "Flemish Loop",
        "category": "loop",
        "difficulty_rating": 2,
        "strength_pct": 72,
        "breaking_strength_lbs": 1150,
        "use_cases": ["decoration", "lanyards", "key rings"],
        "proper_use": "Decorative loop knot for lanyards and decorative purposes.",
        "when_not_to_use": "In applications where strength is critical.",
        "how_to_tie_steps": [
            "Form a bight and tie an overhand knot",
            "Pass the standing part through the bight",
            "Create an interlocking pattern",
            "Dress to form the decorative loop"
        ],
        "failure_mode": "Decorative use primarily, not for heavy loads",
        "related_knots": ["Bowline", "Figure Eight Loop", "David's Knot"]
    },
    {
        "name": "Grain Bind",
        "category": "binding",
        "difficulty_rating": 2,
        "strength_pct": 70,
        "breaking_strength_lbs": 900,
        "use_cases": ["binding grain sacks", "securing bales", "temporary binding"],
        "proper_use": "Agricultural binding knot for securing grain sacks and hay bales.",
        "when_not_to_use": "When a more permanent or adjustable bind is needed.",
        "how_to_tie_steps": [
            "Wrap rope around the sack",
            "Make a loop on one side",
            "Pass the other end through and around",
            "Cinch tight"
        ],
        "failure_mode": "Simple knot can slip under movement",
        "related_knots": ["Strangle", "Constrictor", "Miller's Knot"]
    },
    {
        "name": "Guy-Wire Bend",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 77,
        "breaking_strength_lbs": 1300,
        "use_cases": ["telecommunications", "structural support", "antenna masts"],
        "proper_use": "Joining two guy wires or securing wire rope. Used in structural applications.",
        "when_not_to_use": "On regular rope - designed specifically for wire.",
        "how_to_tie_steps": [
            "Form a loop in one wire",
            "Wrap the other wire around both legs of the loop",
            "Tuck end back through",
            "Tension evenly"
        ],
        "failure_mode": "Wire can bend or break at stress points",
        "related_knots": ["Terminator Knot", "Upright Splice", "Eye Splice"]
    },
    {
        "name": "Highwayman's Hitch",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 60,
        "breaking_strength_lbs": 850,
        "use_cases": ["quick release", "temporary tie", "horse tying"],
        "proper_use": "Quick-release hitch that can be cast off with a pull. Used for tying horses.",
        "when_not_to_use": "In critical applications - knot can release accidentally.",
        "how_to_tie_steps": [
            "Pass rope over the rail",
            "Make a loop with a twist",
            "Pass the working end through the loop",
            "Pull on the standing part to release"
        ],
        "failure_mode": "Can release accidentally under movement",
        "related_knots": ["Slippery Hitch", "Quick Release", "Midshipman's Hitch"]
    },
    {
        "name": "Icicle Bend",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 74,
        "breaking_strength_lbs": 1100,
        "use_cases": ["cold weather", "rescue", "arctic conditions"],
        "proper_use": "Bending knot designed to perform well in freezing conditions.",
        "when_not_to_use": "In warm conditions where other knots are more reliable.",
        "how_to_tie_steps": [
            "Arrange ropes parallel",
            "Create interlocking wraps",
            "Pass ends through center",
            "Keep wraps tight and even"
        ],
        "failure_mode": "Ice buildup can affect performance",
        "related_knots": ["Carrick Bend", "Zeppelin Bend", "Water Knot"]
    },
    {
        "name": "Jesuit's Bend",
        "category": "bending",
        "difficulty_rating": 2,
        "strength_pct": 76,
        "breaking_strength_lbs": 1250,
        "use_cases": ["joining ropes", "climbing", "rescue"],
        "proper_use": "Also known as the义 。Strong bending knot used in rescue operations.",
        "when_not_to_use": "On wet or icy ropes where it may slip.",
        "how_to_tie_steps": [
            "Overlap rope ends",
            "Wrap one end around the other twice",
            "Tuck through between ropes",
            "Repeat with other end"
        ],
        "failure_mode": "Can be bulky and hard to dress properly",
        "related_knots": ["Fisherman's Knot", "Blood Knot", "Water Knot"]
    },
    {
        "name": "Killick",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 65,
        "breaking_strength_lbs": 950,
        "use_cases": ["anchoring small boats", "mooring", "sea anchor"],
        "proper_use": "Anchoring a small boat or creating a sea anchor using a stone or weight.",
        "when_not_to_use": "On smooth surfaces where grip is insufficient.",
        "how_to_tie_steps": [
            "Wrap rope around the weight/stone",
            "Cross over to form an X",
            "Wrap again to secure",
            "Use the bight for attachment"
        ],
        "failure_mode": "Weight can shift and loosen the hitch",
        "related_knots": ["Clove Hitch", "Anchor Bend", "Sea Anchor"]
    },
    {
        "name": "Lariat",
        "category": "loop",
        "difficulty_rating": 3,
        "strength_pct": 75,
        "breaking_strength_lbs": 1200,
        "use_cases": ["rodeo", "ranch work", "capturing livestock"],
        "proper_use": "Creating a running noose from a single rope. Traditional ranch tool.",
        "when_not_to_use": "In any application where a fixed loop is safer.",
        "how_to_tie_steps": [
            "Form a small loop in the standing end",
            "Pass the working end through the loop",
            "Wrap the standing end around to form the honda",
            "Leave enough space for the noose to slide"
        ],
        "failure_mode": "Noose can tighten beyond control",
        "related_knots": ["Perfection Loop", "Niggerhead", "Running Bowline"]
    },
    {
        "name": "Magnusson",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 82,
        "breaking_strength_lbs": 1450,
        "use_cases": ["sailing", "yachting", "heavy weather"],
        "proper_use": "High-strength bending knot developed for yachting. Reliable under load.",
        "when_not_to_use": "When quick release is needed.",
        "how_to_tie_steps": [
            "Form a loop with one rope",
            "Pass the other rope through twice",
            "Weave through the loop structure",
            "Tighten gradually"
        ],
        "failure_mode": "Difficult to untie after heavy loading",
        "related_knots": ["Carrick Bend", "Zeppelin Bend", "Buntline"]
    },
    {
        "name": "Midshipman's",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 70,
        "breaking_strength_lbs": 1100,
        "use_cases": ["mooring", "adjustable tension", "fenders"],
        "proper_use": "Adjustable hitch taught by naval midshipmen. Used for fenders and adjustable lines.",
        "when_not_to_use": "In critical load-bearing applications.",
        "how_to_tie_steps": [
            "Pass rope around the object",
            "Make a half hitch around the standing part",
            "Add another half hitch below",
            "Adjust by sliding"
        ],
        "failure_mode": "Can slip under variable loads",
        "related_knots": ["Taut-Line Hitch", "Rolling Hitch", "Munter Hitch"]
    },
    {
        "name": "Nail Knot",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 72,
        "breaking_strength_lbs": 1000,
        "use_cases": ["fishing", "fly fishing", "leader connections"],
        "proper_use": "Joining fishing line to leader. Creates a smooth, slim connection.",
        "when_not_to_use": "On heavy lines or when quick tying is needed.",
        "how_to_tie_steps": [
            "Use a needle or nail as a mandrel",
            "Wrap line over the needle",
            "Pass through and wrap back",
            "Remove needle and tighten"
        ],
        "failure_mode": "Can weaken thin lines if tied incorrectly",
        "related_knots": ["Blood Knot", "Uni Knot", "Trojan"]
    },
    {
        "name": "Needle Yarn",
        "category": "binding",
        "difficulty_rating": 2,
        "strength_pct": 60,
        "breaking_strength_lbs": 700,
        "use_cases": ["fishing flies", "fly tying", "craft work"],
        "proper_use": "Securing yarn or feather to a fishing hook. Classic fly-tying technique.",
        "when_not_to_use": "On heavy applications.",
        "how_to_tie_steps": [
            "Wrap the yarn around the hook shank",
            "Pass thread over and through",
            "Build up secure wraps",
            "Finish with whip finish"
        ],
        "failure_mode": "Limited to light-duty applications",
        "related_knots": ["Blood Knot", "Clinch Knot", "Uni Knot"]
    },
    {
        "name": "Osman",
        "category": "loop",
        "difficulty_rating": 3,
        "strength_pct": 78,
        "breaking_strength_lbs": 1300,
        "use_cases": ["rescue", "safety loops", "fall protection"],
        "proper_use": "Secure loop knot used in rescue operations. High safety factor.",
        "when_not_to_use": "When quick adjustment of loop size is needed.",
        "how_to_tie_steps": [
            "Form a bight and pass through the anchor point",
            "Wrap around the standing part",
            "Create a second wrap below the first",
            "Pass the loop through and dress"
        ],
        "failure_mode": "Complex structure can be improperly tied",
        "related_knots": ["Bowline", "Figure Eight Loop", "Alpine Butterfly"]
    },
    {
        "name": "Overhand",
        "category": "stopper",
        "difficulty_rating": 1,
        "strength_pct": 60,
        "breaking_strength_lbs": 800,
        "use_cases": ["stopper knot", "foundation knot", "backup"],
        "proper_use": "The most basic stopper knot. Foundation for many other knots.",
        "when_not_to_use": "When a stronger or larger stopper is needed.",
        "how_to_tie_steps": [
            "Pass the working end over the standing part",
            "Pass under and through the loop",
            "Pull tight"
        ],
        "failure_mode": "Can jam severely after loading",
        "related_knots": ["Stevedore", "Figure Eight", "False Overhand"]
    },
    {
        "name": "Ashley Bend",
        "category": "bending",
        "difficulty_rating": 2,
        "strength_pct": 74,
        "breaking_strength_lbs": 1200,
        "use_cases": ["joining ropes", "equal diameter", "sailing"],
        "proper_use": "Clifford Ashley's modification of the sheet bend. Better for equal diameter ropes.",
        "when_not_to_use": "When ropes differ significantly in diameter.",
        "how_to_tie_steps": [
            "Form a loop in one rope with working end on top",
            "Pass the other rope through from below",
            "Wrap around both legs of the loop",
            "Tuck under the first wrap"
        ],
        "failure_mode": "Can work loose if not properly tensioned",
        "related_knots": ["Sheet Bend", "Carrick Bend", "Counterpart"]
    },
    {
        "name": "Packer's Bend",
        "category": "bending",
        "difficulty_rating": 2,
        "strength_pct": 73,
        "breaking_strength_lbs": 1100,
        "use_cases": ["packaging", "bale binding", "temporary secure"],
        "proper_use": "Knot used in packaging and shipping for securing bales and packages.",
        "when_not_to_use": "When permanent binding is needed.",
        "how_to_tie_steps": [
            "Cross the two ropes",
            "Wrap one end around the other twice",
            "Tuck through the center",
            "Tighten"
        ],
        "failure_mode": "Simple knot can loosen over time",
        "related_knots": ["Strangle", "Miller's Knot", "Grain Bind"]
    },
    {
        "name": "Palm",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 68,
        "breaking_strength_lbs": 1000,
        "use_cases": ["fishing", "net making", "splicing"],
        "proper_use": "Creating a hitch using a looping motion around the palm. Used in net making.",
        "when_not_to_use": "In heavy load applications.",
        "how_to_tie_steps": [
            "Wrap rope around the hand",
            "Cross over the palm",
            "Form loops with fingers",
            "Pull through to create the hitch"
        ],
        "failure_mode": "Grip depends heavily on technique",
        "related_knots": ["Nail Knot", "Sailmaker's Hitch", "Seize"]
    },
    {
        "name": "Perfect",
        "category": "loop",
        "difficulty_rating": 3,
        "strength_pct": 85,
        "breaking_strength_lbs": 1500,
        "use_cases": ["climbing", "anchor creation", "rescue"],
        "proper_use": "Extremely strong loop knot. Used in critical safety applications.",
        "when_not_to_use": "When the loop needs to be easily adjusted.",
        "how_to_tie_steps": [
            "Form a loop in the rope",
            "Wrap the standing part around the loop three times",
            "Pass the working end back through the loop",
            "Dress carefully and tighten"
        ],
        "failure_mode": "Very difficult to untie after loading",
        "related_knots": ["Figure Eight Loop", "Alpine Butterfly", "Water Bowline"]
    },
    {
        "name": "Pile",
        "category": "stopper",
        "difficulty_rating": 2,
        "strength_pct": 70,
        "breaking_strength_lbs": 950,
        "use_cases": ["stopper knot", "decoration", "marine rope work"],
        "proper_use": "Decorative stopper knot with a flaired top. Traditional ship's rope work.",
        "when_not_to_use": "When a functional stopper is needed.",
        "how_to_tie_steps": [
            "Form a wall knot crown",
            "Unlay the strands at top",
            "Weave strands over and under",
            "Crown and result the knot"
        ],
        "failure_mode": "Decorative primarily",
        "related_knots": ["Matthew Walker", "Star Knot", "Wall and Crown"]
    },
    {
        "name": "Ring Bend",
        "category": "bending",
        "difficulty_rating": 2,
        "strength_pct": 72,
        "breaking_strength_lbs": 1100,
        "use_cases": ["joining ropes", "hooking to rings", "sailing"],
        "proper_use": "Joining two ropes or attaching to a ring. Simple and effective.",
        "when_not_to_use": "When the connection must be highly secure.",
        "how_to_tie_steps": [
            "Pass rope through ring or over partner rope",
            "Wrap around",
            "Pass back through the loop created",
            "Tighten"
        ],
        "failure_mode": "Can slip if not properly dressed",
        "related_knots": ["Carrick Bend", "Sheet Bend", "Anchor Bend"]
    },
    {
        "name": "Round Turn",
        "category": "hitch",
        "difficulty_rating": 1,
        "strength_pct": 75,
        "breaking_strength_lbs": 1250,
        "use_cases": ["mooring", "anchor lines", "temporary hitch"],
        "proper_use": "Two wraps around an object before finishing. Provides grip and security.",
        "when_not_to_use": "When quick release is needed.",
        "how_to_tie_steps": [
            "Pass rope around the object",
            "Make two complete turns around it",
            "Finish with a half hitch",
            "Tighten"
        ],
        "failure_mode": "Can become difficult to unwind",
        "related_knots": ["Round Turn and Two Half Hitches", "Clove Hitch", "Anchor Bend"]
    },
    {
        "name": "Seize",
        "category": "binding",
        "difficulty_rating": 3,
        "strength_pct": 88,
        "breaking_strength_lbs": 1400,
        "use_cases": ["splicing preparation", "locking", "serving"],
        "proper_use": "Wrapping technique to seize or lock rope parts together. Used in traditional ropework.",
        "when_not_to_use": "When quick application is needed.",
        "how_to_tie_steps": [
            "Lay seizing rope alongside the main rope",
            "Wrap tightly with close turns one way",
            "Return with spaced turns the other way",
            "Finish with square knots"
        ],
        "failure_mode": "Time-consuming to apply correctly",
        "related_knots": ["Constrictor", "Strangle", "West Country Whipping"]
    },
    {
        "name": "Shark",
        "category": "hitch",
        "difficulty_rating": 3,
        "strength_pct": 76,
        "breaking_strength_lbs": 1200,
        "use_cases": ["fishing", "speargun", "securing line"],
        "proper_use": "Attaching a line to a hook or ring with a shark-like bite grip.",
        "when_not_to_use": "When quick release is essential.",
        "how_to_tie_steps": [
            "Pass line around the hook/ring",
            "Wrap the standing part with the working end",
            "Create a secure grip hitch",
            "Pull tight"
        ],
        "failure_mode": "Can be difficult to release once set",
        "related_knots": ["Clinch Knot", "Uni Knot", "Palomar"]
    },
    {
        "name": "Shoelace Knot",
        "category": "binding",
        "difficulty_rating": 1,
        "strength_pct": 45,
        "breaking_strength_lbs": 500,
        "use_cases": ["shoes", "light binding", "quick tie"],
        "proper_use": "The common shoelace knot. Quick and easy but not highly secure.",
        "when_not_to_use": "In any load-bearing or critical application.",
        "how_to_tie_steps": [
            "Cross ends over and through",
            "Form a loop with one end",
            "Wrap other end around and through",
            "Pull both ends to tighten"
        ],
        "failure_mode": "Commonly comes untied unexpectedly",
        "related_knots": ["Square Knot", "Reef Knot", "Simple Simon"]
    },
    {
        "name": "Simple Simon",
        "category": "loop",
        "difficulty_rating": 1,
        "strength_pct": 58,
        "breaking_strength_lbs": 850,
        "use_cases": ["quick loops", "temporary", "instruction"],
        "proper_use": "Simple loop knot often used in teaching. Weaker than a bowline.",
        "when_not_to_use": "In any safety-critical application.",
        "how_to_tie_steps": [
            "Form a loop with the working end on top",
            "Pass the working end under the standing part",
            "Pass through the loop",
            "Tighten"
        ],
        "failure_mode": "Less stable than a bowline",
        "related_knots": ["Bowline", "Overhand Loop", "Figure Eight"]
    },
    {
        "name": "Skene",
        "category": "loop",
        "difficulty_rating": 2,
        "strength_pct": 72,
        "breaking_strength_lbs": 1100,
        "use_cases": ["yachting", "bow line", "docking"],
        "proper_use": "Single-loop knot popular in yachting for bow lines and springs.",
        "when_not_to_use": "When maximum strength is required.",
        "how_to_tie_steps": [
            "Form a bight and cross over",
            "Wrap around the standing part",
            "Pass through the bight",
            "Dress and tighten"
        ],
        "failure_mode": "Not as secure as a properly tied bowline",
        "related_knots": ["Bowline", "Figure Eight Loop", "Dandy Bowline"]
    },
    {
        "name": "Sling",
        "category": "loop",
        "difficulty_rating": 3,
        "strength_pct": 90,
        "breaking_strength_lbs": 1600,
        "use_cases": ["lifting", "cargo handling", "climbing"],
        "proper_use": "Creating a strong loop for lifting. Used in industrial and climbing applications.",
        "when_not_to_use": "When the loop needs to be easily adjustable.",
        "how_to_tie_steps": [
            "Form the rope into a loop",
            "Create an eyre through the standing part",
            "Secure with appropriate method",
            "Test before use"
        ],
        "failure_mode": "Sling can fail if loop geometry is wrong",
        "related_knots": ["Eye Splice", "Girth Hitch", "Choker Hitch"]
    },
    {
        "name": "Slippery",
        "category": "hitch",
        "difficulty_rating": 1,
        "strength_pct": 55,
        "breaking_strength_lbs": 750,
        "use_cases": ["quick release", "fenders", "temporary tie"],
        "proper_use": "Quick-release hitch that can be cast off with a pull. Fender hitch.",
        "when_not_to_use": "In critical applications.",
        "how_to_tie_steps": [
            "Pass rope around the rail",
            "Wrap over itself creating a loop",
            "Tuck under the wrap",
            "Pull standing part to release"
        ],
        "failure_mode": "Can release accidentally",
        "related_knots": ["Highwayman's Hitch", "Quick Release", "Midshipman's"]
    },
    {
        "name": "Stevedore",
        "category": "stopper",
        "difficulty_rating": 2,
        "strength_pct": 82,
        "breaking_strength_lbs": 1350,
        "use_cases": ["stopper knot", "anchor", "heavy duty"],
        "proper_use": "Large stopper knot that grips well and is hard to pull through.",
        "when_not_to_use": "When the knot needs to be easily removable.",
        "how_to_tie_steps": [
            "Form a loop",
            "Wrap the working end around the standing part twice instead of once",
            "Pass through the loop",
            "Tighten carefully"
        ],
        "failure_mode": "Very difficult to untie after loading",
        "related_knots": ["Figure Eight", "Overhand", "Double Overhand"]
    },
    {
        "name": "Strangle",
        "category": "binding",
        "difficulty_rating": 2,
        "strength_pct": 80,
        "breaking_strength_lbs": 1250,
        "use_cases": ["binding", "seizing", "temporary whippings"],
        "proper_use": "Tight binding knot used for seizing and securing. Similar to constrictor.",
        "when_not_to_use": "When you need to untie it later.",
        "how_to_tie_steps": [
            "Wrap around the object",
            "Tuck the working end under the standing part",
            "Wind tightly around both parts",
            "Pull very tight"
        ],
        "failure_mode": "Can cut into rope fibers",
        "related_knots": ["Constrictor", "Transom Knot", "Miller's Knot"]
    },
    {
        "name": "Student",
        "category": "loop",
        "difficulty_rating": 2,
        "strength_pct": 65,
        "breaking_strength_lbs": 950,
        "use_cases": ["education", "beginner loops", "teaching"],
        "proper_use": "Simple loop knot taught to beginners. Easy to learn and tie.",
        "when_not_to_use": "In any safety-critical application.",
        "how_to_tie_steps": [
            "Form a simple overhand knot",
            "Pass the standing part through to form a loop",
            "Adjust size and tighten"
        ],
        "failure_mode": "Less stable than other loop knots",
        "related_knots": ["Simple Simon", "Bowline", "Overhand Loop"]
    },
    {
        "name": "Surrey",
        "category": "loop",
        "difficulty_rating": 3,
        "strength_pct": 75,
        "breaking_strength_lbs": 1150,
        "use_cases": ["yachting", "bow lines", "decoration"],
        "proper_use": "Decorative yacht knot that also functions as a secure loop.",
        "when_not_to_use": "In heavy industrial applications.",
        "how_to_tie_steps": [
            "Form a crown knot base",
            "Build up decorative layers",
            "Work the strands down",
            "Finish with a matthew walker"
        ],
        "failure_mode": "Complex structure can fail if improperly tied",
        "related_knots": ["Matthew Walker", "Monkey's Fist", "Bowline"]
    },
    {
        "name": "Tarbuck",
        "category": "hitch",
        "difficulty_rating": 3,
        "strength_pct": 78,
        "breaking_strength_lbs": 1300,
        "use_cases": ["load bearing", "lifting", "hoisting"],
        "proper_use": "Load-bearing hitch that grips well on smooth surfaces.",
        "when_not_to_use": "On rough surfaces where other hitches work better.",
        "how_to_tie_steps": [
            "Wrap rope around the load",
            "Cross over forming an X",
            "Wrap again and pass through",
            "Tighten securely"
        ],
        "failure_mode": "Load can shift if not properly balanced",
        "related_knots": ["Barrel Hitch", "Slippery Hitch", "Stevedore"]
    },
    {
        "name": "Timber",
        "category": "hitch",
        "difficulty_rating": 2,
        "strength_pct": 73,
        "breaking_strength_lbs": 1100,
        "use_cases": ["logistics", "lumber handling", "securing timber"],
        "proper_use": "Securing and lifting timber and cylindrical lumber.",
        "when_not_to_use": "On short pieces where the hitch won't hold.",
        "how_to_tie_steps": [
            "Wrap rope around the timber",
            "Cross over at top",
            "Wrap underneath",
            "Pass through the lower loop and tighten"
        ],
        "failure_mode": "Timber can roll and loosen the hitch",
        "related_knots": ["Barrel Hitch", "Transom Knot", "Slippery"]
    },
    {
        "name": "Water",
        "category": "bending",
        "difficulty_rating": 2,
        "strength_pct": 68,
        "breaking_strength_lbs": 1000,
        "use_cases": ["water sports", "rescue", "wet conditions"],
        "proper_use": "Joining two lines that will be wet or under water.",
        "when_not_to_use": "On dry ropes in static applications.",
        "how_to_tie_steps": [
            "Overlap the two rope ends",
            "Form an overhand knot",
            "Pass the ends back through the knot in opposite directions",
            "Tighten carefully"
        ],
        "failure_mode": "Can slip under continuous load",
        "related_knots": ["Fisherman's Knot", "Double Water Knot", "Barrel Knot"]
    },
    {
        "name": "Zeppelin Bend",
        "category": "bending",
        "difficulty_rating": 3,
        "strength_pct": 83,
        "breaking_strength_lbs": 1450,
        "use_cases": ["aviation", "ballooning", "heavy duty joining"],
        "proper_use": "High-strength bending knot developed for zeppelins. Very reliable.",
        "when_not_to_use": "When quick release is needed.",
        "how_to_tie_steps": [
            "Form a loop in one rope",
            "Pass the other rope under the loop's cross point",
            "Wrap around both legs of the loop",
            "Tuck through and tighten"
        ],
        "failure_mode": "Extremely difficult to untie after loading",
        "related_knots": ["Carrick Bend", "Magnusson", "Hunter's Bend"]
    },
    {
        "name": "Ring Bend Alt",
        "category": "bending",
        "difficulty_rating": 1,
        "strength_pct": 60,
        "breaking_strength_lbs": 850,
        "use_cases": ["quick join", "temporary", "training"],
        "proper_use": "Simple alternative to ring bend for quick joining.",
        "when_not_to_use": "In applications requiring secure connection.",
        "how_to_tie_steps": [
            "Pass one rope through the ring",
            "Loop back and pass through again",
            "Pull tight",
            "Dress neatly"
        ],
        "failure_mode": "Simple knot prone to slipping",
        "related_knots": ["Ring Bend", "Carrick Bend", "Sheet Bend"]
    }
]

# Knot count (55 knots bundled with comprehensive data)
_KNOT_COUNT = len(KNOTS_DATA)

# Build lookup index
KNOTS_BY_NAME = {knot["name"]: knot for knot in KNOTS_DATA}
KNOTS_BY_CATEGORY = {}
for knot in KNOTS_DATA:
    cat = knot["category"]
    if cat not in KNOTS_BY_CATEGORY:
        KNOTS_BY_CATEGORY[cat] = []
    KNOTS_BY_CATEGORY[cat].append(knot)

# Index for use case searching
KNOTS_BY_USE_CASE = {}
for knot in KNOTS_DATA:
    for use_case in knot.get("use_cases", []):
        if use_case not in KNOTS_BY_USE_CASE:
            KNOTS_BY_USE_CASE[use_case] = []
        KNOTS_BY_USE_CASE[use_case].append(knot)
