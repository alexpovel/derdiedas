# Changelog

## [0.9.1](https://github.com/alexpovel/derdiedas/compare/v0.9.0...v0.9.1) (2022-12-18)


### Bug Fixes

* Remove hover for non-hover-enabled devices (mobile) ([cb032d0](https://github.com/alexpovel/derdiedas/commit/cb032d0cf74ff054b6b8ed2c2947e6104f5de49e))

## [0.9.0](https://github.com/alexpovel/derdiedas/compare/v0.8.1...v0.9.0) (2022-12-13)


### Features

* Also show loading spinner on *initial* word load ([abc0d31](https://github.com/alexpovel/derdiedas/commit/abc0d31ccde369e9950e8c7071ec5c3bb82bf51e))
* Defer JS script loading, provide initial text to prevent content shifting ([5f84f69](https://github.com/alexpovel/derdiedas/commit/5f84f693ca2b6c2b0217b11841877a1501583240))
* gzip responses ([600c73a](https://github.com/alexpovel/derdiedas/commit/600c73ad1b8eb81321234519b2c9d46b8aaafc5c))
* Provide accessible link info ([168f15f](https://github.com/alexpovel/derdiedas/commit/168f15fa7d4b834d3ce64a47e7c8e2a60137b780))
* Provide alt text for images ([f1fc4cb](https://github.com/alexpovel/derdiedas/commit/f1fc4cb51b4cfafee96b27944218a258b61c073d))
* Provide cache busting on every new release ([5a246f4](https://github.com/alexpovel/derdiedas/commit/5a246f45f5dd0656bfb54ec6ff1fafdad133d996))


### Bug Fixes

* Fix link area being larger than contained image itself ([5b23c4d](https://github.com/alexpovel/derdiedas/commit/5b23c4de83ab91f72949b97f0c16e30df0a63b43))

## [0.8.1](https://github.com/alexpovel/derdiedas/compare/v0.8.0...v0.8.1) (2022-12-12)


### Bug Fixes

* Bust cache ([33b6bb3](https://github.com/alexpovel/derdiedas/commit/33b6bb37049f16f5d5ba728adf6bbe66f5112884))

## [0.8.0](https://github.com/alexpovel/derdiedas/compare/v0.7.0...v0.8.0) (2022-12-12)


### Features

* Replace 'Contact' string with GitHub (logo) link ([c1d31e9](https://github.com/alexpovel/derdiedas/commit/c1d31e90a8b2aa90032beb3ed15ee1ff1d421644))

## [0.7.0](https://github.com/alexpovel/derdiedas/compare/v0.6.0...v0.7.0) (2022-12-12)


### Features

* Optimize image sizes ([ce5ddc0](https://github.com/alexpovel/derdiedas/commit/ce5ddc00a4886fc21ba8c3657cb4246570693ffd))


### Documentation

* Fix lie 👀 ([05938de](https://github.com/alexpovel/derdiedas/commit/05938debe346a5fc14f8ac74fe56ccd30add3cf6))

## [0.6.0](https://github.com/alexpovel/derdiedas/compare/v0.5.2...v0.6.0) (2022-12-11)


### Features

* Clean word list (remove wrong, duplicate, ambiguous, outdated or inappropriate entries) ([09de828](https://github.com/alexpovel/derdiedas/commit/09de8284bd0ebf217f135887798228c49818976f)), closes [#6](https://github.com/alexpovel/derdiedas/issues/6)

## [0.5.2](https://github.com/alexpovel/derdiedas/compare/v0.5.1...v0.5.2) (2022-12-11)


### Bug Fixes

* Align input buttons via CSS grid as well, fixing iOS centering issues ([832c6be](https://github.com/alexpovel/derdiedas/commit/832c6be28252017fcde1676f960e472f46bf731b))
* Use correctly-cased input values, saving on case conversions ([0be6a29](https://github.com/alexpovel/derdiedas/commit/0be6a29d0890307dac3fc45b29fde7a62a15ca5d))


### Documentation

* Fix mention of FastAPI -&gt; Starlette ([efa767a](https://github.com/alexpovel/derdiedas/commit/efa767afc8b3ed8ea2e178ecafee945547f8ba82))

## [0.5.1](https://github.com/alexpovel/derdiedas/compare/v0.5.0...v0.5.1) (2022-12-11)


### Bug Fixes

* Center-align form input elements ([7885c72](https://github.com/alexpovel/derdiedas/commit/7885c7205b6004e1e28d956be01ee40cfa04c15b))
* Change `PATCH` -&gt; `GET` ([61adcf3](https://github.com/alexpovel/derdiedas/commit/61adcf30877fb55a95143a0dba4338517eaf407d))
* Fix Safari `text-decoration` with underlining ([cfe4999](https://github.com/alexpovel/derdiedas/commit/cfe4999d8d155ff469d4541dd033b05676493816))
* Grant margins so elements don't touch outer ones ([e09067c](https://github.com/alexpovel/derdiedas/commit/e09067c889bdf78e5acaab43788ffc6ab513706c))
* Properly align left-most article column ([a81d58f](https://github.com/alexpovel/derdiedas/commit/a81d58fc051ad3ee2bf67cc533706fbf6e374c13))
* Unify all titles/names/... to 'Der Die Das?! ([eb49813](https://github.com/alexpovel/derdiedas/commit/eb4981343166cc443697697918a526101eba85df))

## [0.5.0](https://github.com/alexpovel/derdiedas/compare/v0.4.0...v0.5.0) (2022-12-11)


### Features

* Set proper caching headers for static assets ([34f5999](https://github.com/alexpovel/derdiedas/commit/34f59993271d7c206faac008ae755fa94c0abd35))


### Bug Fixes

* site webmanifest icon paths ([1fe5057](https://github.com/alexpovel/derdiedas/commit/1fe505737940f38cff9b5b2413f23978e6faff2e))


### Documentation

* Update static license links ([bf87d8b](https://github.com/alexpovel/derdiedas/commit/bf87d8b6841a9ebeb5b1b605abf63f169149cb12))

## [0.4.0](https://github.com/alexpovel/derdiedas/compare/v0.3.0...v0.4.0) (2022-12-11)


### Features

* Drop `FastAPI`, use `starlette` directly ([317c7ae](https://github.com/alexpovel/derdiedas/commit/317c7aee2293ae3d7d69329fdb3ee04d4870540f))


### Documentation

* Add hint on `poetry` setup ([7b7c16c](https://github.com/alexpovel/derdiedas/commit/7b7c16c0a5c6fa00297f61f6537300b2d291a496))

## [0.3.0](https://github.com/alexpovel/derdiedas/compare/v0.2.0...v0.3.0) (2022-12-11)


### Features

* Add language attribute to elements ([8a7144a](https://github.com/alexpovel/derdiedas/commit/8a7144a91b4b84d59db3f52b8a4cbcc74831ab0a))
* Add meta description to site. ([c800e3d](https://github.com/alexpovel/derdiedas/commit/c800e3d7d1f9b451f94db9b4f95484ae0751a31d))


### Documentation

* Add setup instructions to README ([b586e8f](https://github.com/alexpovel/derdiedas/commit/b586e8fae0c754b64d617f2a2b5a37679274f067))

## [0.2.0](https://github.com/alexpovel/derdiedas/compare/v0.1.0...v0.2.0) (2022-12-10)


### Features

* Add Dockerfile & automatic CI building for it ([45ab8c9](https://github.com/alexpovel/derdiedas/commit/45ab8c9a84f46eae289e085c8a8fefc3c0cc862e))


### Documentation

* Update README ([c276688](https://github.com/alexpovel/derdiedas/commit/c276688614f8a3cdfc97972495a2880d3b29adfb))

## 0.1.0 (2022-12-10)


### Bug Fixes

* Complete rewrite using CSS grids, fixing various issues ([dfd8139](https://github.com/alexpovel/derdiedas/commit/dfd813940d6be0fa73f0462dfbae742748972389))
