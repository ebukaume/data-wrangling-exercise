<h1 align="center">HH gas price data wrangling</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/ebukaume/data-wrangling-exercise#readme" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/ebukaume/data-wrangling-exercise/graphs/commit-activity" target="_blank">
    <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://github.com/ebukaume/data-wrangling-exercise/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/ebukaume/data-wrangling-exercise" />
  </a>
  <a href="https://twitter.com/ebukaume" target="_blank">
    <img alt="Twitter: ebukaume" src="https://img.shields.io/twitter/follow/ebukaume.svg?style=social" />
</p>

<br>

<p>
  <a href="https://data-wrangling-exercise-rails.herokuapp.com/" target="_blank">
    <img alt="Website" src="./docs/facebook.png" />
  </a>
</p>

<br>

The is a simple data wrangling exercise. The aim of this exercise is to scrape Henry Hubs' gas price (both daily and monthly) data from [EIA](http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm), clean it up and present the data in a CSV format. 

As an extra, I have also done a visual representation (line graph) of the price data using D3. 

## Technologies

- Python 3
- Requests
- Beautifulsoup
- html5lib
- D3
- Bootstrap 4x

## Usage

The visualization can be found [here]()

NB: Make sure you have python 3 abd git unstall before moving foward with these steps

```sh
# Clone this repository
$ git clone https://github.com/ebukaume/data-wrangling-exercise.git

# Go into the repository
$ cd data-wrangling-exercise

# Install dependencies
$ pip3 install requests
$ pip3 install beautifulsoup4
$ pip3 install html5lib

# Run the script
$ python3 bin/main.py
```
> To view the visualization locally, you need to start an HTTP server and load the index page in the root.

## Contributing

1. Fork it (https://github.com/ebukume/data-wrangling-exercise/fork)
2. Create your feature branch (git checkout -b feature/[choose-a-name])
3. Commit your changes (git commit -am 'what this commit will fix/add')
4. Push to the branch (git push origin feature/[chosen-name])
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details

## Contact me

_ebukaume@gmail.com_
