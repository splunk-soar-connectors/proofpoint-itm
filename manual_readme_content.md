**TODO**: add support for API call to platform users, get User UUID for use in 'assign user'
**TODO**: check screenshots interface around files<br>
**TODO**: update status / progress movement - nothing around in-progress / close/postivie/negative/beginine yet<br>
**TODO**: get users function defined, but does nothing, should faile, untested, its just a remidner to action

Thanks to **JOHN WANG** of **SPLUNK** - you really made this happen a billion times faster than it would have without you. And it was WAY EASIER for me having you on hand to ask questions of. I bet you are so happy it is done now!<br>
Thanks **ARAVIND** & **ALBERT** & **JOSHUA** for always being online when i just happened to need you<br>

So this app does stuff yea! Well its supposed to<br>

**ACTIONS** as listed in the app... a bucketload of **JSON** is in the get ticket puppy BUT also really cool is the timeline_url that is returned which i generate for you to be able to jump into the timeline of the alert and see whats happening asap<br><br>
There is no check real check for the get files thing, so basically, its really beta, pre-beata, alpha, pre-alpha... anyway go hard or go home right? wait! that doesnt work anymore, every is working from home already... ok - go hard or go to the office! since all we do in the office is socialise and i never get anything more than less than two lunhces, and 50 coffies on a work from office day, this seems right<br><br>

- Added support for oct/stream recognition - use case is download origional email, will expand to support screenshots later<br>
- the timeline_url to the output of get-ticket (need to get the ticket details to calculate the timeline url)<br>
- Added support for assigning owner (need to enhance, currently just a select list of users are pre-configured)<br>
- created oAuth process around token and token use, needs to be made better, we dont reuse token beyond the single call to the app, should at least last the whole playbook run if we call the mapp more than once in a run, but for now...
