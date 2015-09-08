![ristrettogram](https://github.com/ytspar/ristrettogram/blob/master/source/docs/images/logo-heading-general.png)

## What 
Short video clips ([hyperlapse](https://hyperlapse.instagram.com) or timelapse) of third wave coffee shops, pulled from [Instagram](http://instagram.com/ytspar).

## Sketch mockups
Find the specs on Zeplin: [bit.ly/rgzeplin](http://bit.ly/rgzeplin) 

## Tech

- [Middleman](http://middlemanapp.com/) - static site generator
- [HTML5 Boilerplate](http://html5boilerplate.com/)
- [Amicus](https://github.com/nathos/amicus) - excellent Middleman base
- [Livereload](https://middlemanapp.com/basics/development_cycle/) is enabled by default
- [middleman-s3_sync](https://github.com/fredjean/middleman-s3_sync) - for deploying to S3
- [middleman-minify-html](https://github.com/middleman/middleman-minify-html) - for minifying HTML
- [middleman-bower](https://github.com/polleverywhere/middleman_bower) - use the bower package manager
- [Sass mediaqueries](http://github.com/paranoida/sass-mediaqueries) - for adding human readable breakpoints
- [VideoJS](http://www.videojs.com) - HTML5 video player 
- [Moment.js](http://momentjs.com) - for "time ago" timestamps
- [Uptime Robot](https://uptimerobot.com) - for monnitoring the site; basic HTTP ping.

### Markup, styling
- [Haml](http://haml-lang.com/)
- [Sass](http://sass-lang.com/)
- [Compass](http://compass-style.org/)
- [Bourbon](http://bourbon.io) and [Neat](http://neat.bourbon.io) for typography
- [Susy](http://susy.oddbird.net/) - grid system *(not currently using but included)*


## How do I use it?


Start by installing [Bundler](http://gembundler.com/), if you don't already have it:

```
gem install bundler
```

Then, clone the repository down to your local machine:

```
git clone git@github.com:ytspar/ristrettogram.git however_you_want_to_name_your_copy_of_ristrettogram
```

Finally, do a ```bundle install``` to install the required gems -- even Middleman itself.

Add an `aws.yml` file to your root (see [Deployment](https://github.com/ytspar/ristrettogram/wiki/Deployment) in the wiki for details).

Use ```middleman``` to do your live development and ```middleman build``` to render your static file output to the ```/build/``` directory.

Use ```middleman server``` to build dynamically on development.

**Deploy on S3**

See [Deployment](https://github.com/ytspar/ristrettogram/wiki/Deployment) in the wiki.

For full Middleman documentation, visit the [Middleman website](http://middlemanapp.com/).

**Commit format**

From [semantic commit messages](http://seesparkbox.com/foundry/semantic_commit_messages),

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

**Examples**

```
chore: add Oyster build script
docs: explain hat wobble
feat: add beta sequence
fix: remove broken confirmation message
refactor: share logic between 4d3d3d3 and flarhgunnstow
style: convert tabs to spaces
test: ensure Tayne retains clothing
```

To make this easier, use: [git-semantic-commits](https://github.com/fteem/git-semantic-commits)


## Middleman template
*From Amicus docs - have not tested with this repo*

Middleman now supports project templates. To use **ristrettogram** as a template, clone the Git repository into ```~/.middleman```, like so:

```git clone git@github.com:ytspar/ristrettogram.git ~/.middleman/ristrettogram```

then use the new template argument for the ```middleman init``` command:

```middleman init my_new_project --template=ristrettogram```


## What cruft have we included?

[Susy](http://susy.oddbird.net/) is the default grid system. Not currently used, but available.

An included Ruby helper method to generate image placeholders, powered by [Holder.js](http://imsky.github.com/holder/). Haven't used it, but it's there.


## Comments, suggestions?

Send a [message on Github](https://github.com/ytspar) or submit an [issue](https://github.com/ytspar/ristrettogram/issues), or [via Twitter, @ristrettogram](http://twitter.com/ristrettogram).

### To do

Moved to [Issues](https://github.com/ytspar/ristrettogram/issues?q=is%3Aopen+is%3Aissue).

And [a list of possible, nice-to-have features](https://github.com/ytspar/ristrettogram/wiki/Possible-features).


## License

Following the lead of [HTML5 Boilerplate](https://github.com/h5bp/html5-boilerplate) here...

**Major components**

* HTML5 Boilerplate: MIT license
* Normalize.css: MIT license
* Modernizr: MIT/BSD license
* jQuery: MIT/GPL license
* Susy: MIT license

**License**

* MIT license -- see LICENSE.md

### Colophon

On the road between Berlin, Bangkok, Chiang Mai and Pai, among other places. 

**Built using**

- [Sketch](http://www.bohemiancoding.com/sketch/) - design
- [Zeplin](http://zeplin.io) - design specs
- [Sublime](http://www.sublimetext.com) - code
- [Vim](http://www.vim.org) - code, self-loathing
- [Icongen](http://iconogen.com/) - favicons (will be replaced by automated tool)
- [SassToCSS](http://www.sasstoscss.com) - GUI for converting CSS to SASS; quicker than CLI sometimes
- [HTMLtoHAML](http://htmltohaml.com) - same idea as above

