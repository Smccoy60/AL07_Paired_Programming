# Week 5: Memoization, Caching, and Assignment Syntax

Support for Thursday’s memoization demo. The comparison explains terminology; it does not add browser, server, or decorator implementations to AL07.

## 1. Why Save a Calculation?

Suppose a function repeatedly asks for the same subtotal. Once the answer for that input is known, saving it can avoid calculating it again.

**Memoization** stores a function’s result under the input that produced it, then reuses that result when the same input is needed. It is one form of caching. The saved answer must still be valid for everything that affects the result.

In the demo, F(5) asks for F(4) and F(3). Calculating F(4) already calculates F(3), so the later F(3) request can reuse its saved result.

```python
# Excerpt from calculate_cached; n, cache, and counts are its parameters.
if n in cache:
    counts["hits"] += 1
    return cache[n]

# After obtaining result for a new input:
cache[n] = result
```

A **hit** finds a saved answer; a **miss** requires obtaining the answer and storing it. The cache does not eliminate the first calculation for every input. For n=5, both versions return 5; the uncached helper is called 15 times and the cached helper 9 times, including 3 hits, with 6 distinct saved inputs. Counts refer to calculation-helper invocations, including the first invocation; they exclude parser, validation, public wrapper, and display calls.

Each `cached_fibonacci` call creates a new cache/counter dictionary, then shares those objects among its recursive helper calls. There is no global state or hidden enclosing function. This fresh-run choice makes comparisons repeatable; a longer-lived application might deliberately retain its cache between requests.

## 2. “Packed State” Is Assignment Syntax

The old code initialized several variables on one line:

```python
cache, calls, hits = {}, 0, 0
```

This is parallel assignment using unpacking: the three right-hand values are assigned to the three names in order. It does not create a special state object. For clarity, the same initialization can be written:

```python
cache = {}
calls = 0
hits = 0
```

The refactored demo instead uses a cache and a dictionary with named counters:

```python
cache = {}
counts = {"calls": 0, "hits": 0}
```

Returning several values, such as `return result, calls`, packs a tuple. Receiving them with `result, calls = ...` unpacks that tuple. Chained assignment, such as `calls = hits = 0`, assigns one value to multiple names; with mutable objects, `first = second = {}` would share one dictionary. These Python assignment forms are separate from whether an algorithm uses caching. See [Python’s tuple packing and sequence unpacking explanation](https://docs.python.org/3.14/tutorial/datastructures.html#tuples-and-sequences).

## 3. Which Cache Are We Discussing?

The common idea is retaining something for reuse. The owner, contents, matching rule, lifetime, and refresh policy depend on the mechanism.

| Context | What Is Retained? | Who Controls Reuse / Lifetime? |
| --- | --- | --- |
| Demo: Python dictionary memoization | Fibonacci input → calculated result | Our code checks/stores entries; each public call starts fresh. |
| Python `functools.cache` / `lru_cache` | Function results matched by arguments | A decorator provides memoization; `lru_cache` can bound entry count, while `cache` is unbounded; clearing/eviction matters. |
| JavaScript application memory | Results in a `Map` or other application-owned structure | Application code implements the lookup and refresh rule; `Map` alone does not memoize a function. |
| Browser HTTP cache | HTTP responses, such as scripts, stylesheets, or images | Browser/network rules and HTTP headers determine freshness and revalidation. |
| Browser Cache API | Stored Request/Response pairs | Application code explicitly manages entries and freshness; this API does not honor HTTP caching headers automatically. |
| Browser `localStorage` / `sessionStorage` | Application-written string key/value data | Application logic decides what it means; `localStorage` can persist across sessions, while `sessionStorage` is scoped to a page session. Storage alone is not automatic memoization. |

The [Python function-cache documentation](https://docs.python.org/3.14/library/functools.html#functools.cache) and [lru_cache reference](https://docs.python.org/3.14/library/functools.html#functools.lru_cache) describe conveniences beyond the explicit dictionary we implement here. Read decorators as optional recognition, not another coding requirement.

For web connections, see [JavaScript Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), [HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching), [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache), and [Web Storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API). Clearing an HTTP cache and clearing localStorage are different operations. In HTTP, no-cache allows storage but requires revalidation before ordinary cached reuse; no-store directs caches not to store the response.

Server applications can likewise cache computed answers or database-query results; the application must choose its key, lifetime, and refresh policy. Hardware and runtime implementation caches operate at other layers and should not be confused with our explicit function-result dictionary.

## 4. Three Questions to Keep the Meaning Clear

- What exactly is saved, and what identifies a reusable answer?
- How long does it remain available?
- What change would make it stale, and who refreshes or removes it?

For the fixed Fibonacci definition, n identifies the answer. For a stock count or changing price, the same product ID can later need a different answer; cached results need an appropriate key and invalidation/refresh policy. A browser response cache, call stack, stored user preference, and memoized result therefore serve different purposes even when they all retain data.
