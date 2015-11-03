---
layout: post 
title: Installing Python Modules
date: 2012-10-05 00:00:00
category: tutorial
---

One of the great things about using Python is the number of fantastic code libraries that are widely and easily available that can save you a lot of coding. Once these libraries are installed on your computer, you can use them by importing them at the beginning of your code; you can import as many libraries as you'd like, such as

{% highlight python %}
import csv
import requests
import kmlwriter
import pprint
{% endhighlight %}

For new Python users, it can be a bit intimidating to download and install external modules for the first time. There are many ways of doing it; this tutorial covers one of the easiest and most common. This tutorial shows you how to install software on our computer that can automatically download and install Python modules. We'll use a program called [pip](http://www.pip-installer.org/en/latest/).

We can install pip via the command line by using the [curl command](http://www.thegeekstuff.com/2012/04/curl-examples/). As per the pip documentation, we can download a python script to install pip for us.

{% highlight console %}
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py
{% endhighlight %}

once you&#8217;ve downloaded the get-pip.py file, you need to run it in python. if you try to execute the script with python like so

{% highlight console %}
python get-pip.py
{% endhighlight %}

the script will most likely fail because the script won&#8217;t have permissions to update certain directories on your filesystem that are by default set so that random scripts cannot change important files and give you viruses. In this case, and in all cases where you need to allow a script that you trust to write to your system folders, you can use the sudo command (short for &#8220;Super User DO&#8221;) in front of the python command, like

{% highlight bash %}
sudo python get-pip.py
{% endhighlight %}

In sum, the below two lines should get and execute the pip installer script.

{% highlight bash %}
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
{% endhighlight %}

If you want to be even fancier, we can combine these by using the Linux &#8216;pipe&#8217; command (|), which automatically sends the output of one command to another. So executing

{% highlight bash %}
curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo python
{% endhighlight %}

will download the get-pip.py script with the curl command, then use that script as an argument for the sudo python command, which is equivalent to what we did above in two separate steps. 

Now that you have pip, it is easy to install python modules. Usually when you find a module that you want to use, the installation instructions will have the necessary pip command, such as

{% highlight bash %}
pip install requests
pip install beautifulsoup4
pip install simplekml
{% endhighlight %}

Remember, for the same reasons explained above, you will probably need to run pip with sudo, like

{% highlight bash %}
sudo pip install requests
{% endhighlight %}

Once you've installed the library you want, be sure to include them in the beginning of each python file in which you want to use the library.