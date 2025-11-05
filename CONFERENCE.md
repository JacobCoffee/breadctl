# Conference Talk notes

> ntoe: is live demo, ohh scary 👻!

### Setup (5 mins before talk)

1. Ensure Python 3.14 with PEP 810 is working
2. Run `make bench` to generate fresh results
3. Open `benchmark-results.md` for reference
4. Have two terminal windows ready:
    - Left: normal version
    - Right: lazy version
5. if all breaks during talk, unplug pc, run away

### Live Demo Flow

**0. Intro our bread ~~smuggling~~ operation business (2 min)**

**1. Show the Problem (2 min)**
```bash
# Terminal 1
time uv run breadctl --help
# Takes ~150ms, loads all modules
```

problem: shit is slow

**2. Explain PEP 810 (3 min)**
- Show `src/breadctl/lazy.py` with `lazy import` syntax
- Explain deferred loading behavior

very nice, but how does it work?


**3. Show the Solution (2 min)**
```bash
# Terminal 2
time uv run breadctl-lazy --help
# Takes ~40ms, only loads click/rich
```

no more problem. okay, is still slow but like.. not as bad right?

**4. Deep Dive (5 min)**
```bash
# Show import tree comparison
python -X importtime -c "import breadctl.normal" 2>&1 | head -20
python -X importtime -c "import breadctl.lazy" 2>&1 | head -20
```

idk if this is right way

**5. Run Hyperfine Benchmark (3 min)**
```bash
make bench
# Show visual comparison to wow audience
cat benchmark-results.md
```

**6. Explain When to Use (5 min)**
- CLI tools with many subcommands (litestar 😉)
- Large test suites
- Services with optional features
- Applications with plugin systems (litestar 😉)

**7. Caveats (2 min)**
- Import-time side effects are deferred
- Need to test for changed behavior
- Tooling support still evolving

**8. Q&A**
lol no thanks im shy and some person from an interpreter team at a quant firm will
ask me something i don't know how to answer

## Key Talking Points

### Why Lazy Imports Matter

todo: update

- **CLI Tools**: `--help` shouldn't load heavyweight dependencies
- **Test Suites**: Faster test discovery and collection
- **Microservices**: Reduced cold-start time in serverless
- **Developer Experience**: Clearer than manual `if TYPE_CHECKING:` blocks

### PEP 810 Design Principles

todo: update 

1. **Explicit**: Uses `lazy` keyword, no surprises
2. **Local**: Only affects the specific import statement
3. **Granular**: Per-import control, not global flag

### Migration Strategy

1. Profile current import time (`python -X importtime`)
2. Identify heavy/rarely-used modules
3. Apply `lazy import` selectively
4. Test for side-effect timing changes
5. Measure improvement with Hyperfine
6. CLI go brrrrr 🚀

## Resources

- [PEP 810 - Explicit Lazy Imports](https://peps.python.org/pep-0810/)
- [Python Import System](https://docs.python.org/3/reference/import.html)
- [Building CPython][building-cpython]
- [Hyperfine Benchmarking](https://github.com/sharkdp/hyperfine)

[building-cpython]: https://docs.python.org/3/reference/import.html

## Open questions

- do we want to deep dive into the pep810 implementation?
 - do i know enough about this 😵‍💫
- similar but for PyImport_ stuff
- similar but for AST building around the new `lazy` kw
