# twitterSnipper
<p>This Python3 script filters tweets with the (roughly) same wording as previous ones from a twitter list.</p>

## Setting Up

### Short Version
<p><ul>
<li>install 'tweepy' module (3.5.0)</li>
<li>create a file 'keys.py' with your twitter credentials</li>
<li>provide values for mySlug and maxNumberOfTweets via sys.argv[1] and sys.argv[2] respectively, OR customize 'mySlug' and 'maxNumberOfTweets' values in the script</li>
</ul></p>


### Long Version
<p><b>1.)</b> You will need to register as a twitter developer on apps.twitter.com (it's free) to get the authentication keys, etc. Create a file 'keys.py' in the same directory as where you put 'twitterSnipper.py'. Set the variables mentioned in 'from keys import' to the values generated for you by twitter. If you're lost, <i><a href="http://www.codecademy.com" target="_blank">CodeCademy.com</a></i> has a tutorial 'Using the Twitter API' with a section 'Authenticating with Twitter' which guides you through the steps.</p>

<p><b>2.)</b> You will also need to have the <i>tweepy</i> module installed. I'm running it on version 3.5.0 Get it from PyPI via</p>

<pre><code>pip install tweepy
</code></pre>

<p>Or if you're on a Mac:</p>

<pre><code>pip3 install tweepy
</code></pre>

<p><b>3.)</b> If you have only <b>one list</b> to filter, set 'maxNumberOfTweets' to the number of tweets you want to filter from. If you want to filter from all new tweets since you last checked (or the maximum number of new tweets allowed by the twitter API), set "maxNumberOfTweets = None". For example:</p>

<pre><code>mySlug = 'newsfeed'
maxNumberOfTweets = 100
</code></pre>

<p>Set 'mySlug' to the name of the twitter list you want to filter. If you're not sure what the slug is, click on the list and then have a look at the URL. It should be something like: 
<br /><a href="#">https://twitter.com/YourTwitterHandle/lists/NameOfYourList</a>
<br />The last part ('NameOfYourList') should be your slug.</p>

<p>In your shell, change to the directory you keep your script in, then run it via</p>

<pre><code>python twitterSnipper.py 
</code></pre>

<p>(remember to use 'python3' if you're on a Mac.)
<br>
<br>
If you have <b>several lists</b> to filter, provide values for 'mySlug' (see above) and 'maxNumberOfTweets' via the shell when you run the script. For example:</p>

<pre><code>python twitterSnipper.py newsfeed 50
</code></pre>

<p>In that case, you'll be retrieving the 50 latest tweets from a list 'newsfeed' and filtering those.
<br>
<br>
Sidenote: If you haven't used the shell yet and/or are intimidated by it, maybe check out Zed Shaw's <a href="https://learnpythonthehardway.org/book/appendixa.html">Command Line Crash Course</a>. Hope that helps!</p>

<p>4.) Display the tweets either by just opening the .txt file by double clicking it in your folder or display the contents directly in your shell via 'cat YourTwitterHandle_YourSlug.txt'. For example:</p>

<pre><code>cat franaitch_newsfeed.txt
</code></pre>

<p>Tip: a quick way to open a link in your browser is to just right click on the url, then click 'Open URL'. </p>

## Please Note
<p>I deleted my twitter account, so some of the most recent changes to the script are untested. Should work, but let me know if it doesn't.</p>

## Feedback
<p>I just recently started coding. Any feedback on how to make my code more elegant and/or efficient would be much appreciated!</p>

## Thanks
<p>To @glacoste. Your twitter-cleaner helped me to get started.</p>
