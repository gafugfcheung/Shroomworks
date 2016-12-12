// DESCRIBES FEED ITEM AND ADDS INFORMATION
function createFeedItem(src, location, title, time, likes) {
  var content = "";
  content += '<div class="newsfeed-item" onClick="IDtoFullScreen(';
  content += srcToID[src];
  content += ')"><img class="newsfeed-photo" src="';
  content += src;
  content += '"><div class="newsfeed-item-topbar"><div class="newsfeed-item-location newsfeed-item-minor">';
  content += location;
  content += '</div><div class="newsfeed-item-title">';
  content += title;
  content += '</div><div class="newsfeed-item-time newsfeed-item-minor">';
  content += time;
  content += '</div></div><div class="newsfeed-item-bottombar"><div class="newsfeed-item-likes">';
  content += likes;
  content += '</div></div></div>';
  addToNewsFeed(content);
}
