![ristrettogram](https://dl.dropboxusercontent.com/u/225019/ristrettogram-logo.png)

# ristrettogram

## What 
Short video clips ([hyperlapse](https://hyperlapse.instagram.com) or timelapse) of third wave coffee shops, pulled from [Instagram](http://instagram.com/ytspar).

## Tech

- [Middleman](http://middlemanapp.com/) - static site generator
- [HTML5 Boilerplate](http://html5boilerplate.com/)
- [Amicus](https://github.com/nathos/amicus) - excellent Middleman base
- [Livereload](https://middlemanapp.com/basics/development_cycle/) is enabled by default
- [SassToCSS](http://www.sasstoscss.com)

### Markup
- [Haml](http://haml-lang.com/)

### CSS
- [Sass](http://sass-lang.com/)
- [Compass](http://compass-style.org/)
- [Bourbon](http://bourbon.io) and [Neat](http://neat.bourbon.io) for typography
- [Susy](http://susy.oddbird.net/) - grid system *(not currently using but included)*


## How do I use it?

*(from the Amicus docs)*

Start by installing [Bundler](http://gembundler.com/), if you don't already have it:

```
gem install bundler
```

Then, clone the repository down to your local machine:

```
git clone git@github.com:ytspar/ristrettogram.git however_you_want_to_name_your_copy_of_ristrettogram
```

Finally, do a ```bundle install``` to install the required gems -- even Middleman itself.

Use ```middleman``` to do your live development and ```middleman build``` to render your static file output to the ```/build/``` directory.

Use ```middleman server``` to build dynamically on development.

**Deploy on S3**

`[PENDING]`

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
**In no particular order,**

**Planned**

- Test on retina (need 2x, 3x, whatever? SVG?)
- Generate cities table dynamically from YAML files
- Compress/minify CSS, Javascript
- Production deploy to S3, Route53 config
- Bower/Gulp process to replace locked in place HTML5 boilerplate and so on
- Add Google Analytics, heatmap etc (Segment?)
- Favicon
- Apple touch icons
- Press kit with high res assets

*Views*

- City view
- City files with Instagram links
- Static content view for about, terms
- Contribute form
- Tablet versions (use [Breakpoint Sass](http://breakpoint-sass.com)?)

---
- Oh yeah, content!

**Maybe?**

- Make slightly fluid columns? that is, make the main container, say 87.5% width, max width like 375 or iPhone 6 dimensions
- Buy short domain?
- README: change the header image to one in the repo? (`![Alt text](/relative/path/to/img.jpg?raw=true "Optional Title"`)


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
- [Sublime](http://www.sublimetext.com) - code
