<!DOCTYPE html>
<html lang="en">
<head>
  <meta id="bb-bootstrap" data-current-user="{&quot;isKbdShortcutsEnabled&quot;: true, &quot;isSshEnabled&quot;: false, &quot;isAuthenticated&quot;: false}" />
  
  
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta charset="utf-8">
  <title>
  wswp / code 
  / source  / chapter03 / downloader.py
 &mdash; Bitbucket
</title>
  <script type="text/javascript">window.NREUM||(NREUM={}),__nr_require=function(e,t,n){function r(n){if(!t[n]){var o=t[n]={exports:{}};e[n][0].call(o.exports,function(t){var o=e[n][1][t];return r(o||t)},o,o.exports)}return t[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(e,t,n){function r(){}function o(e,t,n){return function(){return i(e,[(new Date).getTime()].concat(u(arguments)),t?null:this,n),t?void 0:this}}var i=e("handle"),a=e(2),u=e(3),c=e("ee").get("tracer"),f=NREUM;"undefined"==typeof window.newrelic&&(newrelic=f);var s=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",p=l+"ixn-";a(s,function(e,t){f[t]=o(l+t,!0,"api")}),f.addPageAction=o(l+"addPageAction",!0),f.setCurrentRouteName=o(l+"routeName",!0),t.exports=newrelic,f.interaction=function(){return(new r).get()};var d=r.prototype={createTracer:function(e,t){var n={},r=this,o="function"==typeof t;return i(p+"tracer",[Date.now(),e,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[Date.now(),r,o],n),o)try{return t.apply(this,arguments)}finally{c.emit("fn-end",[Date.now()],n)}}}};a("setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,t){d[t]=o(p+t)}),newrelic.noticeError=function(e){"string"==typeof e&&(e=new Error(e)),i("err",[e,(new Date).getTime()])}},{}],2:[function(e,t,n){function r(e,t){var n=[],r="",i=0;for(r in e)o.call(e,r)&&(n[i]=t(r,e[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],3:[function(e,t,n){function r(e,t,n){t||(t=0),"undefined"==typeof n&&(n=e?e.length:0);for(var r=-1,o=n-t||0,i=Array(o<0?0:o);++r<o;)i[r]=e[t+r];return i}t.exports=r},{}],ee:[function(e,t,n){function r(){}function o(e){function t(e){return e&&e instanceof r?e:e?c(e,u,i):i()}function n(n,r,o){if(!p.aborted){e&&e(n,r,o);for(var i=t(o),a=v(n),u=a.length,c=0;c<u;c++)a[c].apply(i,r);var f=s[w[n]];return f&&f.push([y,n,r,i]),i}}function d(e,t){b[e]=v(e).concat(t)}function v(e){return b[e]||[]}function g(e){return l[e]=l[e]||o(n)}function m(e,t){f(e,function(e,n){t=t||"feature",w[n]=t,t in s||(s[t]=[])})}var b={},w={},y={on:d,emit:n,get:g,listeners:v,context:t,buffer:m,abort:a,aborted:!1};return y}function i(){return new r}function a(){(s.api||s.feature)&&(p.aborted=!0,s=p.backlog={})}var u="nr@context",c=e("gos"),f=e(2),s={},l={},p=t.exports=o();p.backlog=s},{}],gos:[function(e,t,n){function r(e,t,n){if(o.call(e,t))return e[t];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[t]=r,r}var o=Object.prototype.hasOwnProperty;t.exports=r},{}],handle:[function(e,t,n){function r(e,t,n,r){o.buffer([e],r),o.emit(e,t,n)}var o=e("ee").get("handle");t.exports=r,r.ee=o},{}],id:[function(e,t,n){function r(e){var t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");t.exports=r},{}],loader:[function(e,t,n){function r(){if(!h++){var e=y.info=NREUM.info,t=l.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&t))return f.abort();c(b,function(t,n){e[t]||(e[t]=n)}),u("mark",["onload",a()],null,"api");var n=l.createElement("script");n.src="https://"+e.agent,t.parentNode.insertBefore(n,t)}}function o(){"complete"===l.readyState&&i()}function i(){u("mark",["domContent",a()],null,"api")}function a(){return(new Date).getTime()}var u=e("handle"),c=e(2),f=e("ee"),s=window,l=s.document,p="addEventListener",d="attachEvent",v=s.XMLHttpRequest,g=v&&v.prototype;NREUM.o={ST:setTimeout,CT:clearTimeout,XHR:v,REQ:s.Request,EV:s.Event,PR:s.Promise,MO:s.MutationObserver},e(1);var m=""+location,b={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1016.min.js"},w=v&&g&&g[p]&&!/CriOS/.test(navigator.userAgent),y=t.exports={offset:a(),origin:m,features:{},xhrWrappable:w};l[p]?(l[p]("DOMContentLoaded",i,!1),s[p]("load",r,!1)):(l[d]("onreadystatechange",o),s[d]("onload",r)),u("mark",["firstbyte",a()],null,"api");var h=0},{}]},{},["loader"]);</script>
  


<meta id="bb-canon-url" name="bb-canon-url" content="https://bitbucket.org">

<meta name="bb-commit-hash" content="c4a7121149e9">
<meta name="bb-app-node" content="app-104">
<meta name="bb-view-name" content="bitbucket.apps.repo2.views.filebrowse">
<meta name="ignore-whitespace" content="False">
<meta name="tab-size" content="None">
<meta name="locale" content="en">

<meta name="application-name" content="Bitbucket">
<meta name="apple-mobile-web-app-title" content="Bitbucket">
<meta name="theme-color" content="#205081">
<meta name="msapplication-TileColor" content="#205081">
<meta name="msapplication-TileImage" content="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/img/logos/bitbucket/white-256.png">
<link rel="apple-touch-icon" sizes="192x192" type="image/png" href="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/img/bitbucket_avatar/192/bitbucket.png">
<link rel="icon" sizes="192x192" type="image/png" href="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/img/bitbucket_avatar/192/bitbucket.png">
<link rel="icon" sizes="16x16 32x32" type="image/x-icon" href="/favicon.ico">
<link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket">
  <meta name="description" content="">
  
  
    
  



  <link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/css/entry/vendor.css" />
<link rel="stylesheet" href="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/css/entry/app.css" />




  
  <script src="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/dist/webpack/early.js"></script>
  
  
    <link href="/wswp/code/rss" rel="alternate nofollow" type="application/rss+xml" title="RSS feed for code" />

</head>
<body class="production aui-page-sidebar aui-sidebar-expanded"
    data-static-url="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/"
data-base-url="https://bitbucket.org"
data-base-api-url="https://api.bitbucket.org"
data-no-avatar-image="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/img/default_avatar/user_blue.svg"
data-current-user="{&quot;isKbdShortcutsEnabled&quot;: true, &quot;isSshEnabled&quot;: false, &quot;isAuthenticated&quot;: false}"
data-atlassian-id="{&quot;loginStatusUrl&quot;: &quot;https://id.atlassian.com/profile/rest/profile&quot;}"
data-settings="{&quot;MENTIONS_MIN_QUERY_LENGTH&quot;: 3}"


data-current-repo="{&quot;scm&quot;: &quot;hg&quot;, &quot;readOnly&quot;: false, &quot;mainbranch&quot;: {&quot;name&quot;: &quot;default&quot;}, &quot;language&quot;: &quot;python&quot;, &quot;owner&quot;: {&quot;username&quot;: &quot;wswp&quot;, &quot;uuid&quot;: &quot;9fb81ab8-181b-4c0a-8bea-130d71c4f963&quot;, &quot;isTeam&quot;: false}, &quot;fullslug&quot;: &quot;wswp/code&quot;, &quot;slug&quot;: &quot;code&quot;, &quot;id&quot;: 10725179, &quot;pygmentsLanguage&quot;: &quot;python&quot;}"
data-current-cset="9e6b82b47087c2ada0e9fdf4f5e037e151975f0f"





data-browser-monitoring="true"
data-switch-create-pullrequest-commit-status="true"

data-track-js-errors="true"

data-hide-inbox="true">
<div id="page">
  
    
    <div id="wrapper">
      
  


      
        <header id="header" role="banner" data-module="header/tracking">
          
  


          <nav class="aui-header aui-dropdown2-trigger-group" role="navigation">
            <div class="aui-header-inner">
              <div class="aui-header-primary">
                
  

                
                  <h1 class="aui-header-logo aui-header-logo-bitbucket logged-out"
                      id="logo" data-ct="header.logo">
                    <a href="/">
                      <span class="aui-header-logo-device">Bitbucket</span>
                    </a>
                  </h1>
                
                
  

    
    
  

    
    
  
<ul class="aui-nav">
  
    <li>
      <a href="/product/features">
        Features
      </a>
    </li>
    <li>
      <a href="/plans">
        Pricing
      </a>
    </li>
  
</ul>

              </div>
              <div class="aui-header-secondary">
                
  

<ul role="menu" class="aui-nav">
  
  <li>
    <form action="/repo/all" method="get" class="aui-quicksearch">
      <label for="search-query" class="assistive">owner/repository</label>
      <input id="search-query" class="bb-repo-typeahead" type="text"
             placeholder="Find a repository&hellip;" name="name" autocomplete="off"
             data-bb-typeahead-focus="false">
    </form>
  </li>
  <li>
    <a id="help-menu-link" class="aui-nav-link" href="#"
        aria-controls="help-menu-dialog"
        data-aui-trigger>
      <span id="help-menu-icon" class="aui-icon aui-icon-small aui-iconfont-help"></span>
    </a>
  </li>
  
    <li>
      <a class="aui-dropdown2-trigger" href="#header-language"
          aria-controls="header-language" aria-owns="header-language"
          aria-haspopup="true" data-container="#header .aui-header-inner">
        <span>English</span></a>
      <nav id="header-language" class="aui-dropdown2 aui-style-default aui-dropdown2-radio aui-dropdown2-in-header"
          aria-hidden="true">
        <form method="post" action="/account/language/setlang/"
            data-module="i18n/header-language-form">
          <input type="hidden" name="language" value="">
          <ul>
          <li><a class="aui-dropdown2-radio interactive checked"
                data-value="en" href="#en">English</a></li>
          
          <li><a class="aui-dropdown2-radio interactive "
                data-value="ja" href="#ja">日本語</a></li>
          </ul>
        </form>
      </nav>
    </li>
  
  
      <li id="header-signup-button">
        <a id="sign-up-link" data-ct="header.signup" class="aui-button aui-button-primary" href="/account/signup/">
          Sign up
        </a>
      </li>
    <li id="user-options">
      <a href="/account/signin/?next=/wswp/code/src/tip/chapter03/downloader.py" class="aui-nav-link login-link">Log in</a>
    </li>
  
</ul>

              </div>
            </div>
          </nav>
        </header>
      

      
  

<header id="account-warning" role="banner" data-module="header/account-warning"
        class="aui-message-banner warning
        ">
  <div class="aui-message-banner-inner">
    <span class="aui-icon aui-icon-warning"></span>
    <span class="message">
    
    </span>
  </div>
</header>



      
  
<header id="aui-message-bar">
  
</header>


    <div id="content" role="main">
      
        
  
    <div class="aui-sidebar repo-sidebar"
    data-module="repo/sidebar"
  >
  <div class="aui-sidebar-wrapper">
    <div class="aui-sidebar-body">
      <header class="aui-page-header">
        <div class="aui-page-header-inner">
          <div class="aui-page-header-image">
            <a href="/wswp/code" id="repo-avatar-link" class="repo-link">
              <span class="aui-avatar aui-avatar-large aui-avatar-project">
                <span class="aui-avatar-inner">
                  <img src="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/img/repo-avatars/python.svg" alt="">
                </span>
              </span>
            </a>
          </div>
          <div class="aui-page-header-main">
            <h1>
              
              <a href="/wswp/code" title="code" class="entity-name">code</a>
            </h1>
          </div>
        </div>
      </header>
      <nav class="aui-navgroup aui-navgroup-vertical">
        <div class="aui-navgroup-inner">
          
            
              <div class="aui-sidebar-group aui-sidebar-group-actions repository-actions forks-enabled">
                <div class="aui-nav-heading">
                  <strong>Actions</strong>
                </div>
                <ul id="repo-actions" class="aui-nav">
                  
                  
                    <li>
                      <a id="repo-clone-button" class="aui-nav-item "
                        href="#clone"
                        data-ct="sidebar.actions.repository.clone"
                        data-ct-data=""
                        data-module="components/clone/clone-dialog"
                        target="_self">
                        
                          <span class="aui-icon aui-icon-large icon-clone"></span>
                        
                        <span class="aui-nav-item-label">Clone</span>
                      </a>
                    </li>
                  
                    <li>
                      <a id="repo-compare-link" class="aui-nav-item "
                        href="/wswp/code/branches/compare"
                        data-ct="sidebar.actions.repository.compare"
                        data-ct-data=""
                        
                        target="_self">
                        
                          <span class="aui-icon aui-icon-large aui-icon-small aui-iconfont-devtools-compare"></span>
                        
                        <span class="aui-nav-item-label">Compare</span>
                      </a>
                    </li>
                  
                    <li>
                      <a id="repo-fork-link" class="aui-nav-item "
                        href="/wswp/code/fork"
                        data-ct="sidebar.actions.repository.fork"
                        data-ct-data=""
                        
                        target="_self">
                        
                          <span class="aui-icon aui-icon-large icon-fork"></span>
                        
                        <span class="aui-nav-item-label">Fork</span>
                      </a>
                    </li>
                  
                </ul>
              </div>
          
          <div class="aui-sidebar-group aui-sidebar-group-tier-one repository-sections">
            <div class="aui-nav-heading">
              <strong>Navigation</strong>
            </div>
            <ul class="aui-nav">
              
              
                <li>
                  <a id="repo-overview-link" class="aui-nav-item "
                    href="/wswp/code/overview"
                    data-ct="sidebar.navigation.repository.overview"
                    data-ct-data=""
                    
                    target="_self"
                    >
                    
                    
                      <span class="aui-icon aui-icon-large icon-overview"></span>
                    
                    <span class="aui-nav-item-label">
                      Overview
                      
                      
                    </span>
                  </a>
                </li>
              
                <li class="aui-nav-selected">
                  <a id="repo-source-link" class="aui-nav-item "
                    href="/wswp/code/src"
                    data-ct="sidebar.navigation.repository.source"
                    data-ct-data=""
                    
                    target="_self"
                    >
                    
                    
                      <span class="aui-icon aui-icon-large icon-source"></span>
                    
                    <span class="aui-nav-item-label">
                      Source
                      
                      
                    </span>
                  </a>
                </li>
              
                <li>
                  <a id="repo-commits-link" class="aui-nav-item "
                    href="/wswp/code/commits/"
                    data-ct="sidebar.navigation.repository.commits"
                    data-ct-data=""
                    
                    target="_self"
                    >
                    
                    
                      <span class="aui-icon aui-icon-large icon-commits"></span>
                    
                    <span class="aui-nav-item-label">
                      Commits
                      
                      
                    </span>
                  </a>
                </li>
              
                <li>
                  <a id="repo-branches-link" class="aui-nav-item "
                    href="/wswp/code/branches/"
                    data-ct="sidebar.navigation.repository.branches"
                    data-ct-data=""
                    
                    target="_self"
                    >
                    
                    
                      <span class="aui-icon aui-icon-large icon-branches"></span>
                    
                    <span class="aui-nav-item-label">
                      Branches
                      
                      
                    </span>
                  </a>
                </li>
              
                <li>
                  <a id="repo-pullrequests-link" class="aui-nav-item "
                    href="/wswp/code/pull-requests/"
                    data-ct="sidebar.navigation.repository.pullrequests"
                    data-ct-data=""
                    
                    target="_self"
                    >
                    
                      <span class="aui-badge" title="6 open pull requests" id="pullrequests-count">6</span>
                    
                    
                      <span class="aui-icon aui-icon-large icon-pull-requests"></span>
                    
                    <span class="aui-nav-item-label">
                      Pull requests
                      
                      
                    </span>
                  </a>
                </li>
              
                <li>
                  <a id="repo-issues-link" class="aui-nav-item "
                    href="/wswp/code/issues?status=new&amp;status=open"
                    data-ct="sidebar.navigation.issues"
                    data-ct-data=""
                    
                    target="_self"
                    title="( type &#39;r&#39; then &#39;i&#39; )">
                    
                      <span class="aui-badge" title="3 active issues" id="issues-count">3</span>
                    
                    
                      <span class="aui-icon aui-icon-large icon-issues"></span>
                    
                    <span class="aui-nav-item-label">
                      Issues
                      
                      
                    </span>
                  </a>
                </li>
              
                <li>
                  <a id="repo-downloads-link" class="aui-nav-item "
                    href="/wswp/code/downloads/"
                    data-ct="sidebar.navigation.repository.downloads"
                    data-ct-data=""
                    
                    target="_self"
                    >
                    
                    
                      <span class="aui-icon aui-icon-large icon-downloads"></span>
                    
                    <span class="aui-nav-item-label">
                      Downloads
                      
                      
                    </span>
                  </a>
                </li>
              
            </ul>
          </div>
          <div class="aui-sidebar-group aui-sidebar-group-tier-one repository-settings">
            <div class="aui-nav-heading">
              <strong class="assistive">Settings</strong>
            </div>
            <ul class="aui-nav">
              
              
            </ul>
          </div>
          
            
              <div class="hidden kb-shortcut-actions">
                <a id="repo-create-issue" href="/wswp/code/issues/new"></a>
              </div>
            
          
        </div>
      </nav>
    </div>
    <div class="aui-sidebar-footer">
      <a class="aui-sidebar-toggle aui-sidebar-footer-tipsy aui-button aui-button-subtle"><span class="aui-icon"></span></a>
    </div>
  </div>
  

<div id="repo-clone-dialog" class="clone-dialog hidden">
  





  

<div class="clone-url" data-module="components/clone/url-dropdown" data-owner="9fb81ab8-181b-4c0a-8bea-130d71c4f963"
     data-location-context="header"
     data-fetch-url="https://bitbucket.org/wswp/code"
     data-push-url="https://bitbucket.org/wswp/code"
     
     
     
     >
  <div class="aui-buttons">
    
    <button class="aui-button aui-dropdown2-trigger protocol-trigger"
            data-command-prefix="hg clone"
            data-primary-https="https://bitbucket.org/wswp/code"
            data-primary-ssh="ssh://hg@bitbucket.org/wswp/code"
            aria-controls="protocols-list-header">
      <span class="dropdown-text">HTTPS</span>
    </button>
    <aui-dropdown-menu id="protocols-list-header" data-aui-alignment="bottom left">
      <aui-section id="protocols-list-section" class="aui-list-truncate">
        <aui-item-radio class="item-link https" checked>HTTPS</aui-item-radio>
        <aui-item-radio class="item-link ssh">SSH</aui-item-radio>
      </aui-section>
    </aui-dropdown-menu>
    <input type="text" readonly="readonly" class="clone-url-input"
           value="hg clone https://bitbucket.org/wswp/code">
  </div>
  
</div>

  <div class="learn-more">
    <p>Need help cloning? Learn how to
         <a href="https://confluence.atlassian.com/x/4whODQ" target="_blank">clone a repository</a>.
    </p>
  </div>
  
  <div class="sourcetree-callout clone-in-sourcetree"
  data-module="components/clone/clone-in-sourcetree"
  data-https-url="https://bitbucket.org/wswp/code"
  data-ssh-url="ssh://hg@bitbucket.org/wswp/code">

  <div>
    <button class="aui-button aui-button-primary">
      
        Clone in SourceTree
      
    </button>
  </div>

  <p class="windows-text">
    
      <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_win" target="_blank">Atlassian SourceTree</a>
      is a free Git and Mercurial client for Windows.
    
  </p>
  <p class="mac-text">
    
      <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_mac" target="_blank">Atlassian SourceTree</a>
      is a free Git and Mercurial client for Mac.
    
  </p>
</div>
</div>
</div>
  

        
  <div class="aui-page-panel ">
    
  
  
    <div class="aui-page-panel-inner">
      <div id="repo-content" class="aui-page-panel-content"
          data-module="repo/index"
          
          >
        
          
            <ol class="aui-nav aui-nav-breadcrumbs">
              <li>
  <a href="/wswp/">Web Scraping With Python</a>
</li>

<li>
  <a href="/wswp/code">code</a>
</li>
              
            </ol>
          
          <div class="aui-group repo-page-header">
            <div class="aui-item section-title">
              <h1>Source</h1>
            </div>
            <div class="aui-item page-actions">
              
            </div>
          </div>
        
        
  <div id="source-container" class="maskable" data-module="repo/source/index">
    



<header id="source-path">
  
    <div class="labels labels-csv">
      <div class="aui-buttons">
        <button data-branches-tags-url="/api/1.0/repositories/wswp/code/branches-tags"
                data-module="components/branch-dialog"
                class="aui-button branch-dialog-trigger" title="default">
          
            
              <span class="aui-icon aui-icon-small aui-iconfont-devtools-branch">Branch</span>
            
            <span class="name">default</span>
          
          <span class="aui-icon-dropdown"></span>
        </button>
        <button class="aui-button" id="checkout-branch-button"
                title="Check out this branch">
          <span class="aui-icon aui-icon-small aui-iconfont-devtools-clone">Check out branch</span>
          <span class="aui-icon-dropdown"></span>
        </button>
      </div>
      
    
    
  
    </div>
  
  
    <div class="secondary-actions">
      <div class="aui-buttons">
        
          <a href="/wswp/code/src/9e6b82b47087/chapter03/downloader.py?at=default"
            class="aui-button pjax-trigger" aria-pressed="true">
            Source
          </a>
          <a href="/wswp/code/diff/chapter03/downloader.py?diff2=9e6b82b47087&at=default"
            class="aui-button pjax-trigger"
            title="Diff to previous change">
            Diff
          </a>
          <a href="/wswp/code/history-node/9e6b82b47087/chapter03/downloader.py?at=default"
            class="aui-button pjax-trigger">
            History
          </a>
        
      </div>
    </div>
  
  <h1>
    
      
        <a href="/wswp/code/src/9e6b82b47087?at=default"
          class="pjax-trigger root" title="wswp/code at 9e6b82b47087">code</a> /
      
      
        
          
            <a href="/wswp/code/src/9e6b82b47087/chapter03/?at=default"
              class="pjax-trigger directory-name">chapter03</a> /
          
        
      
        
          
            <span class="file-name">downloader.py</span>
          
        
      
    
  </h1>
  
    
    
  
  <div class="clearfix"></div>
</header>


  
    
  

  <div id="editor-container" class="maskable"
       data-module="repo/source/editor"
       data-owner="wswp"
       data-slug="code"
       data-is-writer="false"
       data-has-push-access="true"
       data-hash="9e6b82b47087c2ada0e9fdf4f5e037e151975f0f"
       data-branch="default"
       data-path="chapter03/downloader.py"
       data-source-url="/api/internal/repositories/wswp/code/src/9e6b82b47087c2ada0e9fdf4f5e037e151975f0f/chapter03/downloader.py">
    <div id="source-view" class="file-source-container" data-module="repo/source/view-file" data-is-lfs="false">
      <div class="toolbar">
        <div class="primary">
          <div class="aui-buttons">
            
              <button id="file-history-trigger" class="aui-button aui-button-light changeset-info"
                      data-changeset="9e6b82b47087c2ada0e9fdf4f5e037e151975f0f"
                      data-path="chapter03/downloader.py"
                      data-current="9e6b82b47087c2ada0e9fdf4f5e037e151975f0f">
                 

  <div class="aui-avatar aui-avatar-xsmall">
    <div class="aui-avatar-inner">
      <img src="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/img/default_avatar/user_blue.svg">
    </div>
  </div>
  <span class="changeset-hash">9e6b82b</span>
  <time datetime="2015-09-28T13:29:54+00:00" class="timestamp"></time>
  <span class="aui-icon-dropdown"></span>

              </button>
            
          </div>
          
          <a href="/wswp/code/full-commit/9e6b82b47087/chapter03/downloader.py" id="full-commit-link"
             title="View full commit 9e6b82b">Full commit</a>
        </div>
        <div class="secondary">
          
          <div class="aui-buttons">
            
              <a href="/wswp/code/annotate/9e6b82b47087c2ada0e9fdf4f5e037e151975f0f/chapter03/downloader.py?at=default"
                 class="aui-button aui-button-light pjax-trigger">Blame</a>
              
                
                <a data-embed-url="https://bitbucket.org/wswp/code/src/9e6b82b47087c2ada0e9fdf4f5e037e151975f0f/chapter03/downloader.py?embed=t" class="aui-button aui-button-light js-embed-link">
                  Embed
                </a>
              
            
            <a href="/wswp/code/raw/9e6b82b47087c2ada0e9fdf4f5e037e151975f0f/chapter03/downloader.py" class="aui-button aui-button-light">Raw</a>
          </div>
          
            <button id="file-edit-button" class="edit-button aui-button aui-button-light" disabled="disabled" aria-disabled="true">
              Edit
              <span class="edit-button-overlay" title="Log in to edit this file"></span>
            </button>
          
        </div>

        <div id="fileview-dropdown"
            class="aui-dropdown2 aui-style-default"
            data-fileview-container="#fileview-container"
            
            
            data-fileview-button="#fileview-trigger"
            data-module="connect/fileview">
          <div class="aui-dropdown2-section">
            <ul>
              <li>
                <a class="aui-dropdown2-radio aui-dropdown2-checked"
                    data-fileview-id="-1"
                    data-fileview-loaded="true"
                    data-fileview-target="#fileview-original"
                    data-fileview-connection-key=""
                    data-fileview-module-key="file-view-default">
                  Default File Viewer
                </a>
              </li>
              
            </ul>
          </div>
        </div>

        <div class="clearfix"></div>
      </div>
      <div id="fileview-container">
        <div id="fileview-original"
            class="fileview"
            data-module="repo/source/highlight-lines"
            data-fileview-loaded="true">
          


  
    <div class="file-source">
      <table class="codehilite highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#downloader.py-1"> 1</a>
<a href="#downloader.py-2"> 2</a>
<a href="#downloader.py-3"> 3</a>
<a href="#downloader.py-4"> 4</a>
<a href="#downloader.py-5"> 5</a>
<a href="#downloader.py-6"> 6</a>
<a href="#downloader.py-7"> 7</a>
<a href="#downloader.py-8"> 8</a>
<a href="#downloader.py-9"> 9</a>
<a href="#downloader.py-10">10</a>
<a href="#downloader.py-11">11</a>
<a href="#downloader.py-12">12</a>
<a href="#downloader.py-13">13</a>
<a href="#downloader.py-14">14</a>
<a href="#downloader.py-15">15</a>
<a href="#downloader.py-16">16</a>
<a href="#downloader.py-17">17</a>
<a href="#downloader.py-18">18</a>
<a href="#downloader.py-19">19</a>
<a href="#downloader.py-20">20</a>
<a href="#downloader.py-21">21</a>
<a href="#downloader.py-22">22</a>
<a href="#downloader.py-23">23</a>
<a href="#downloader.py-24">24</a>
<a href="#downloader.py-25">25</a>
<a href="#downloader.py-26">26</a>
<a href="#downloader.py-27">27</a>
<a href="#downloader.py-28">28</a>
<a href="#downloader.py-29">29</a>
<a href="#downloader.py-30">30</a>
<a href="#downloader.py-31">31</a>
<a href="#downloader.py-32">32</a>
<a href="#downloader.py-33">33</a>
<a href="#downloader.py-34">34</a>
<a href="#downloader.py-35">35</a>
<a href="#downloader.py-36">36</a>
<a href="#downloader.py-37">37</a>
<a href="#downloader.py-38">38</a>
<a href="#downloader.py-39">39</a>
<a href="#downloader.py-40">40</a>
<a href="#downloader.py-41">41</a>
<a href="#downloader.py-42">42</a>
<a href="#downloader.py-43">43</a>
<a href="#downloader.py-44">44</a>
<a href="#downloader.py-45">45</a>
<a href="#downloader.py-46">46</a>
<a href="#downloader.py-47">47</a>
<a href="#downloader.py-48">48</a>
<a href="#downloader.py-49">49</a>
<a href="#downloader.py-50">50</a>
<a href="#downloader.py-51">51</a>
<a href="#downloader.py-52">52</a>
<a href="#downloader.py-53">53</a>
<a href="#downloader.py-54">54</a>
<a href="#downloader.py-55">55</a>
<a href="#downloader.py-56">56</a>
<a href="#downloader.py-57">57</a>
<a href="#downloader.py-58">58</a>
<a href="#downloader.py-59">59</a>
<a href="#downloader.py-60">60</a>
<a href="#downloader.py-61">61</a>
<a href="#downloader.py-62">62</a>
<a href="#downloader.py-63">63</a>
<a href="#downloader.py-64">64</a>
<a href="#downloader.py-65">65</a>
<a href="#downloader.py-66">66</a>
<a href="#downloader.py-67">67</a>
<a href="#downloader.py-68">68</a>
<a href="#downloader.py-69">69</a>
<a href="#downloader.py-70">70</a>
<a href="#downloader.py-71">71</a>
<a href="#downloader.py-72">72</a>
<a href="#downloader.py-73">73</a>
<a href="#downloader.py-74">74</a>
<a href="#downloader.py-75">75</a>
<a href="#downloader.py-76">76</a>
<a href="#downloader.py-77">77</a>
<a href="#downloader.py-78">78</a>
<a href="#downloader.py-79">79</a>
<a href="#downloader.py-80">80</a>
<a href="#downloader.py-81">81</a>
<a href="#downloader.py-82">82</a>
<a href="#downloader.py-83">83</a>
<a href="#downloader.py-84">84</a>
<a href="#downloader.py-85">85</a>
<a href="#downloader.py-86">86</a>
<a href="#downloader.py-87">87</a>
<a href="#downloader.py-88">88</a>
<a href="#downloader.py-89">89</a>
<a href="#downloader.py-90">90</a>
<a href="#downloader.py-91">91</a>
<a href="#downloader.py-92">92</a></pre></div></td><td class="code"><div class="codehilite highlight"><pre><span></span><a name="downloader.py-1"></a><span class="kn">import</span> <span class="nn">urlparse</span>
<a name="downloader.py-2"></a><span class="kn">import</span> <span class="nn">urllib2</span>
<a name="downloader.py-3"></a><span class="kn">import</span> <span class="nn">random</span>
<a name="downloader.py-4"></a><span class="kn">import</span> <span class="nn">time</span>
<a name="downloader.py-5"></a><span class="kn">from</span> <span class="nn">datetime</span> <span class="kn">import</span> <span class="n">datetime</span><span class="p">,</span> <span class="n">timedelta</span>
<a name="downloader.py-6"></a><span class="kn">import</span> <span class="nn">socket</span>
<a name="downloader.py-7"></a>
<a name="downloader.py-8"></a>
<a name="downloader.py-9"></a><span class="n">DEFAULT_AGENT</span> <span class="o">=</span> <span class="s1">&#39;wswp&#39;</span>
<a name="downloader.py-10"></a><span class="n">DEFAULT_DELAY</span> <span class="o">=</span> <span class="mi">5</span>
<a name="downloader.py-11"></a><span class="n">DEFAULT_RETRIES</span> <span class="o">=</span> <span class="mi">1</span>
<a name="downloader.py-12"></a><span class="n">DEFAULT_TIMEOUT</span> <span class="o">=</span> <span class="mi">60</span>
<a name="downloader.py-13"></a>
<a name="downloader.py-14"></a>
<a name="downloader.py-15"></a><span class="k">class</span> <span class="nc">Downloader</span><span class="p">:</span>
<a name="downloader.py-16"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="o">=</span><span class="n">DEFAULT_DELAY</span><span class="p">,</span> <span class="n">user_agent</span><span class="o">=</span><span class="n">DEFAULT_AGENT</span><span class="p">,</span> <span class="n">proxies</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">num_retries</span><span class="o">=</span><span class="n">DEFAULT_RETRIES</span><span class="p">,</span> <span class="n">timeout</span><span class="o">=</span><span class="n">DEFAULT_TIMEOUT</span><span class="p">,</span> <span class="n">opener</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">cache</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="downloader.py-17"></a>        <span class="n">socket</span><span class="o">.</span><span class="n">setdefaulttimeout</span><span class="p">(</span><span class="n">timeout</span><span class="p">)</span>
<a name="downloader.py-18"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">throttle</span> <span class="o">=</span> <span class="n">Throttle</span><span class="p">(</span><span class="n">delay</span><span class="p">)</span>
<a name="downloader.py-19"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">user_agent</span> <span class="o">=</span> <span class="n">user_agent</span>
<a name="downloader.py-20"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">proxies</span> <span class="o">=</span> <span class="n">proxies</span>
<a name="downloader.py-21"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">num_retries</span> <span class="o">=</span> <span class="n">num_retries</span>
<a name="downloader.py-22"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">opener</span> <span class="o">=</span> <span class="n">opener</span>
<a name="downloader.py-23"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">cache</span> <span class="o">=</span> <span class="n">cache</span>
<a name="downloader.py-24"></a>
<a name="downloader.py-25"></a>
<a name="downloader.py-26"></a>    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">):</span>
<a name="downloader.py-27"></a>        <span class="n">result</span> <span class="o">=</span> <span class="bp">None</span>
<a name="downloader.py-28"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="p">:</span>
<a name="downloader.py-29"></a>            <span class="k">try</span><span class="p">:</span>
<a name="downloader.py-30"></a>                <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="p">[</span><span class="n">url</span><span class="p">]</span>
<a name="downloader.py-31"></a>            <span class="k">except</span> <span class="ne">KeyError</span><span class="p">:</span>
<a name="downloader.py-32"></a>                <span class="c1"># url is not available in cache </span>
<a name="downloader.py-33"></a>                <span class="k">pass</span>
<a name="downloader.py-34"></a>            <span class="k">else</span><span class="p">:</span>
<a name="downloader.py-35"></a>                <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">num_retries</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="mi">500</span> <span class="o">&lt;=</span> <span class="n">result</span><span class="p">[</span><span class="s1">&#39;code&#39;</span><span class="p">]</span> <span class="o">&lt;</span> <span class="mi">600</span><span class="p">:</span>
<a name="downloader.py-36"></a>                    <span class="c1"># server error so ignore result from cache and re-download</span>
<a name="downloader.py-37"></a>                    <span class="n">result</span> <span class="o">=</span> <span class="bp">None</span>
<a name="downloader.py-38"></a>        <span class="k">if</span> <span class="n">result</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
<a name="downloader.py-39"></a>            <span class="c1"># result was not loaded from cache so still need to download</span>
<a name="downloader.py-40"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">throttle</span><span class="o">.</span><span class="n">wait</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
<a name="downloader.py-41"></a>            <span class="n">proxy</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">proxies</span><span class="p">)</span> <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">proxies</span> <span class="k">else</span> <span class="bp">None</span>
<a name="downloader.py-42"></a>            <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;User-agent&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">user_agent</span><span class="p">}</span>
<a name="downloader.py-43"></a>            <span class="n">result</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">download</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="p">,</span> <span class="n">proxy</span><span class="o">=</span><span class="n">proxy</span><span class="p">,</span> <span class="n">num_retries</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">num_retries</span><span class="p">)</span>
<a name="downloader.py-44"></a>            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="p">:</span>
<a name="downloader.py-45"></a>                <span class="c1"># save result to cache</span>
<a name="downloader.py-46"></a>                <span class="bp">self</span><span class="o">.</span><span class="n">cache</span><span class="p">[</span><span class="n">url</span><span class="p">]</span> <span class="o">=</span> <span class="n">result</span>
<a name="downloader.py-47"></a>        <span class="k">return</span> <span class="n">result</span><span class="p">[</span><span class="s1">&#39;html&#39;</span><span class="p">]</span>
<a name="downloader.py-48"></a>
<a name="downloader.py-49"></a>
<a name="downloader.py-50"></a>    <span class="k">def</span> <span class="nf">download</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="p">,</span> <span class="n">proxy</span><span class="p">,</span> <span class="n">num_retries</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="downloader.py-51"></a>        <span class="k">print</span> <span class="s1">&#39;Downloading:&#39;</span><span class="p">,</span> <span class="n">url</span>
<a name="downloader.py-52"></a>        <span class="n">request</span> <span class="o">=</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">Request</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">headers</span> <span class="ow">or</span> <span class="p">{})</span>
<a name="downloader.py-53"></a>        <span class="n">opener</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">opener</span> <span class="ow">or</span> <span class="n">urllib2</span><span class="o">.</span><span class="n">build_opener</span><span class="p">()</span>
<a name="downloader.py-54"></a>        <span class="k">if</span> <span class="n">proxy</span><span class="p">:</span>
<a name="downloader.py-55"></a>            <span class="n">proxy_params</span> <span class="o">=</span> <span class="p">{</span><span class="n">urlparse</span><span class="o">.</span><span class="n">urlparse</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">scheme</span><span class="p">:</span> <span class="n">proxy</span><span class="p">}</span>
<a name="downloader.py-56"></a>            <span class="n">opener</span><span class="o">.</span><span class="n">add_handler</span><span class="p">(</span><span class="n">urllib2</span><span class="o">.</span><span class="n">ProxyHandler</span><span class="p">(</span><span class="n">proxy_params</span><span class="p">))</span>
<a name="downloader.py-57"></a>        <span class="k">try</span><span class="p">:</span>
<a name="downloader.py-58"></a>            <span class="n">response</span> <span class="o">=</span> <span class="n">opener</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">request</span><span class="p">)</span>
<a name="downloader.py-59"></a>            <span class="n">html</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<a name="downloader.py-60"></a>            <span class="n">code</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">code</span>
<a name="downloader.py-61"></a>        <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
<a name="downloader.py-62"></a>            <span class="k">print</span> <span class="s1">&#39;Download error:&#39;</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">e</span><span class="p">)</span>
<a name="downloader.py-63"></a>            <span class="n">html</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>
<a name="downloader.py-64"></a>            <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="s1">&#39;code&#39;</span><span class="p">):</span>
<a name="downloader.py-65"></a>                <span class="n">code</span> <span class="o">=</span> <span class="n">e</span><span class="o">.</span><span class="n">code</span>
<a name="downloader.py-66"></a>                <span class="k">if</span> <span class="n">num_retries</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="mi">500</span> <span class="o">&lt;=</span> <span class="n">code</span> <span class="o">&lt;</span> <span class="mi">600</span><span class="p">:</span>
<a name="downloader.py-67"></a>                    <span class="c1"># retry 5XX HTTP errors</span>
<a name="downloader.py-68"></a>                    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="p">,</span> <span class="n">proxy</span><span class="p">,</span> <span class="n">num_retries</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>
<a name="downloader.py-69"></a>            <span class="k">else</span><span class="p">:</span>
<a name="downloader.py-70"></a>                <span class="n">code</span> <span class="o">=</span> <span class="bp">None</span>
<a name="downloader.py-71"></a>        <span class="k">return</span> <span class="p">{</span><span class="s1">&#39;html&#39;</span><span class="p">:</span> <span class="n">html</span><span class="p">,</span> <span class="s1">&#39;code&#39;</span><span class="p">:</span> <span class="n">code</span><span class="p">}</span>
<a name="downloader.py-72"></a>
<a name="downloader.py-73"></a>
<a name="downloader.py-74"></a><span class="k">class</span> <span class="nc">Throttle</span><span class="p">:</span>
<a name="downloader.py-75"></a>    <span class="sd">&quot;&quot;&quot;Throttle downloading by sleeping between requests to same domain</span>
<a name="downloader.py-76"></a><span class="sd">    &quot;&quot;&quot;</span>
<a name="downloader.py-77"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">delay</span><span class="p">):</span>
<a name="downloader.py-78"></a>        <span class="c1"># amount of delay between downloads for each domain</span>
<a name="downloader.py-79"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">delay</span> <span class="o">=</span> <span class="n">delay</span>
<a name="downloader.py-80"></a>        <span class="c1"># timestamp of when a domain was last accessed</span>
<a name="downloader.py-81"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">domains</span> <span class="o">=</span> <span class="p">{}</span>
<a name="downloader.py-82"></a>        
<a name="downloader.py-83"></a>    <span class="k">def</span> <span class="nf">wait</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">url</span><span class="p">):</span>
<a name="downloader.py-84"></a>        <span class="sd">&quot;&quot;&quot;Delay if have accessed this domain recently</span>
<a name="downloader.py-85"></a><span class="sd">        &quot;&quot;&quot;</span>
<a name="downloader.py-86"></a>        <span class="n">domain</span> <span class="o">=</span> <span class="n">urlparse</span><span class="o">.</span><span class="n">urlsplit</span><span class="p">(</span><span class="n">url</span><span class="p">)</span><span class="o">.</span><span class="n">netloc</span>
<a name="downloader.py-87"></a>        <span class="n">last_accessed</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">domains</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">domain</span><span class="p">)</span>
<a name="downloader.py-88"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">delay</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">last_accessed</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
<a name="downloader.py-89"></a>            <span class="n">sleep_secs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">delay</span> <span class="o">-</span> <span class="p">(</span><span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span> <span class="o">-</span> <span class="n">last_accessed</span><span class="p">)</span><span class="o">.</span><span class="n">seconds</span>
<a name="downloader.py-90"></a>            <span class="k">if</span> <span class="n">sleep_secs</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
<a name="downloader.py-91"></a>                <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="n">sleep_secs</span><span class="p">)</span>
<a name="downloader.py-92"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">domains</span><span class="p">[</span><span class="n">domain</span><span class="p">]</span> <span class="o">=</span> <span class="n">datetime</span><span class="o">.</span><span class="n">now</span><span class="p">()</span>
</pre></div>
</td></tr></table>
    </div>
  


        </div>
        
      </div>
    </div>
  </div>
  
  <div data-module="source/set-changeset" data-hash="9e6b82b47087c2ada0e9fdf4f5e037e151975f0f"></div>



  
    
    
    
  
  

  </div>

        
        
        
      </div>
    </div>
  </div>

      </div>
    </div>
  

  
    
      <footer id="footer" role="contentinfo" data-module="components/footer">
        <section class="footer-body">
          
  <ul>
  <li>
    <a class="support-ga" target="_blank"
       data-support-gaq-page="Blog"
       href="http://blog.bitbucket.org">Blog</a>
  </li>
  <li>
    <a class="support-ga" target="_blank"
       data-support-gaq-page="Home"
       href="/support">Support</a>
  </li>
  <li>
    <a class="support-ga"
       data-support-gaq-page="PlansPricing"
       href="/plans">Plans &amp; pricing</a>
  </li>
  <li>
    <a class="support-ga" target="_blank"
       data-support-gaq-page="DocumentationHome"
       href="//confluence.atlassian.com/display/BITBUCKET">Documentation</a>
  </li>
  <li>
    <a class="support-ga" target="_blank"
       data-support-gaq-page="DocumentationAPI"
       href="https://developer.atlassian.com/bitbucket/api/2/reference/">API</a>
  </li>
  <li>
    <a class="support-ga" target="_blank"
       data-support-gaq-page="SiteStatus"
       href="https://status.bitbucket.org/">Site status</a>
  </li>
  <li>
    <a class="support-ga" id="meta-info"
       data-support-gaq-page="MetaInfo"
       href="#">Version info</a>
  </li>
  <li>
    <a class="support-ga" target="_blank"
       data-support-gaq-page="EndUserAgreement"
       href="//www.atlassian.com/legal/customer-agreement?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=footer">Terms of service</a>
  </li>
  <li>
    <a class="support-ga" target="_blank"
       data-support-gaq-page="PrivacyPolicy"
       href="//www.atlassian.com/legal/privacy-policy">Privacy policy</a>
  </li>
</ul>
<div id="meta-info-content" style="display: none;">
  <ul>
    
      <li>English</li>
    
    <li>
      <a class="support-ga" target="_blank"
         data-support-gaq-page="GitDocumentation"
         href="http://git-scm.com/">Git 2.7.4.1.g5468f9e</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
         data-support-gaq-page="HgDocumentation"
         href="https://www.mercurial-scm.org">Mercurial 3.9.2</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
         data-support-gaq-page="DjangoDocumentation"
         href="https://www.djangoproject.com/">Django 1.9.12</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
         data-support-gaq-page="PythonDocumentation"
         href="http://www.python.org/">Python 2.7.3</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
         data-support-gaq-page="DeployedVersion"
         data-media-hex="c4a7121149e9"
         href="#">c4a7121149e9 / c4a7121149e9 @ app-104</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
         data-support-gaq-page="StorageRegion"
         href="#">Region production</a>
    </li>
  </ul>
</div>
<ul class="atlassian-links">
  <li>
    <a id="atlassian-jira-link" target="_blank"
       title="Track everything – bugs, tasks, deadlines, code – and pull reports to stay informed."
       href="https://www.atlassian.com/software/jira/bitbucket-integration?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">JIRA Software</a>
  </li>
  <li>
    <a id="atlassian-confluence-link" target="_blank"
       title="Content Creation, Collaboration & Knowledge Sharing for Teams."
       href="http://www.atlassian.com/software/confluence/overview/team-collaboration-software?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Confluence</a>
  </li>
  <li>
    <a id="atlassian-bamboo-link" target="_blank"
       title="Continuous integration and deployment, release management."
       href="http://www.atlassian.com/software/bamboo?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Bamboo</a>
  </li>
  <li>
    <a id="atlassian-sourcetree-link" target="_blank"
       title="A free Git and Mercurial desktop client for Mac or Windows."
       href="http://www.sourcetreeapp.com/?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">SourceTree</a>
  </li>
  <li>
    <a id="atlassian-hipchat-link" target="_blank"
       title="Group chat and IM built for teams."
       href="http://www.hipchat.com/?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">HipChat</a>
  </li>
</ul>
<div id="footer-logo">
  <a target="_blank"
     title="Bitbucket is developed by Atlassian in Austin, San Francisco, and Sydney."
     href="http://www.atlassian.com?utm_source=bitbucket&amp;utm_medium=logo&amp;utm_campaign=bitbucket_footer">Atlassian</a>
</div>

        </section>
      </footer>
    
  
</div>



  

<div data-module="components/mentions/index">
  
    
    
  
  
    
    
  
  
    
    
  
</div>
<div data-module="components/typeahead/emoji/index">
  
    
    
  
</div>

<div data-module="components/repo-typeahead/index">
  
    
    
  
</div>

    
    
  

    
    
  

    
    
  

    
    
  


  


    
    
  

    
    
  



  
  
  <aui-inline-dialog
    id="help-menu-dialog"
    data-aui-alignment="bottom right"

    
    data-aui-alignment-static="true"
    data-module="header/help-menu"
    responds-to="toggle"
    aria-hidden="true">

  <div id="help-menu-section">
    <h1 class="help-menu-heading">Help</h1>

    <form id="help-menu-search-form" class="aui" target="_blank" method="get"
        action="https://support.atlassian.com/customer/search">
      <span id="help-menu-search-icon" class="aui-icon aui-icon-large aui-iconfont-search"></span>
      <input id="help-menu-search-form-input" name="q" class="text" type="text" placeholder="Ask a question">
    </form>

    <ul id="help-menu-links">
      <li>
        <a class="support-ga" data-support-gaq-page="DocumentationHome"
            href="https://confluence.atlassian.com/x/bgozDQ" target="_blank">
          Online help
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="GitTutorials"
            href="https://www.atlassian.com/git?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=help_dropdown&amp;utm_content=learn_git"
            target="_blank">
          Learn Git
        </a>
      </li>
      <li>
        <a id="keyboard-shortcuts-link"
           href="#">Keyboard shortcuts</a>
      </li>
      <li>
        <a href="/whats-new/" id="features-link">
          Latest features
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="DocumentationTutorials"
            href="https://confluence.atlassian.com/x/Q4sFLQ" target="_blank">
          Bitbucket tutorials
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="SiteStatus"
            href="https://status.bitbucket.org/" target="_blank">
          Site status
        </a>
      </li>
      <li>
        <a class="support-ga" data-support-gaq-page="Home" href="/support">
          Support
        </a>
      </li>
    </ul>
  </div>
</aui-inline-dialog>
  






  

  <div class="_mustache-templates">
    
      <script id="repo-dropdown-template" type="text/html">
        


[[#hasViewed]]
  <div class="aui-dropdown2-section">
    <strong class="viewed">Recently viewed</strong>
    <ul>
      [[#viewed]]
        <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
          <a href="[[url]]" title="[[owner]][[#project]] / [[project]][[/project]] / [[name]]" class="aui-icon-container recently-viewed repo-link"
              data-ct="header.repository.dropdown.repository" data-ct-data='{"type": "recently-viewed"}'>
            <span class="aui-avatar aui-avatar-xsmall aui-avatar-project">
              <span class="aui-avatar-inner">
                <img src="[[{avatar}]]">
              </span>
            </span>
            <span class="dropdown-path">
              <span class="dropdown-path-part">[[#project]][[project]][[/project]][[^project]][[owner]][[/project]]</span>
              <span class="dropdown-path-separator">/</span>
              <span class="dropdown-path-part dropdown-path-part--primary">[[name]]</span>
            </span>
          </a>
        </li>
      [[/viewed]]
    </ul>
  </div>
[[/hasViewed]]
[[#hasUpdated]]
  <div class="aui-dropdown2-section">
    <strong class="updated">Recently updated</strong>
    <ul>
      [[#updated]]
      <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
        <a href="[[url]]" title="[[owner]][[#project]] / [[project]][[/project]] / [[name]]" class="aui-icon-container recently-updated repo-link"
           data-ct="header.repository.dropdown.repository" data-ct-data='{"type": "recently-updated"}'>
          <span class="aui-avatar aui-avatar-xsmall aui-avatar-project">
            <span class="aui-avatar-inner">
              <img src="[[{avatar}]]">
            </span>
          </span>
          <span class="dropdown-path">
            <span class="dropdown-path-part">[[#project]][[project]][[/project]][[^project]][[owner]][[/project]]</span>
            <span class="dropdown-path-separator">/</span>
            <span class="dropdown-path-part dropdown-path-part--primary">[[name]]</span>
          </span>
        </a>
      </li>
      [[/updated]]
    </ul>
  </div>
[[/hasUpdated]]

      </script>
    
      <script id="snippet-dropdown-template" type="text/html">
        <div class="aui-dropdown2-section">
  <strong>[[sectionTitle]]</strong>
  <ul class="aui-list-truncate">
    [[#snippets]]
      <li>
        <a href="[[links.html.href]]">[[owner.display_name]] / [[name]]</a>
      </li>
    [[/snippets]]
  </ul>
</div>

      </script>
    
      <script id="branch-checkout-template" type="text/html">
        

<div id="checkout-branch-contents">
  <div class="command-line">
    <p>
      Check out this branch on your local machine to begin working on it.
    </p>
    <input type="text" class="checkout-command" readonly="readonly"
        
          value="hg pull && hg update [[branchName]]"
        
        >
  </div>
  
    <div class="sourcetree-callout clone-in-sourcetree"
  data-module="components/clone/clone-in-sourcetree"
  data-https-url="https://bitbucket.org/wswp/code"
  data-ssh-url="ssh://hg@bitbucket.org/wswp/code">

  <div>
    <button class="aui-button aui-button-primary">
      
        Check out in SourceTree
      
    </button>
  </div>

  <p class="windows-text">
    
      <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_win" target="_blank">Atlassian SourceTree</a>
      is a free Git and Mercurial client for Windows.
    
  </p>
  <p class="mac-text">
    
      <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_mac" target="_blank">Atlassian SourceTree</a>
      is a free Git and Mercurial client for Mac.
    
  </p>
</div>
  
</div>

      </script>
    
      <script id="branch-dialog-template" type="text/html">
        

<div class="tabbed-filter-widget branch-dialog">
  <div class="tabbed-filter">
    <input placeholder="Filter branches" class="filter-box" autosave="branch-dropdown-10725179" type="text">
    [[^ignoreTags]]
      <div class="aui-tabs horizontal-tabs aui-tabs-disabled filter-tabs">
        <ul class="tabs-menu">
          <li class="menu-item active-tab"><a href="#branches">Branches</a></li>
          <li class="menu-item"><a href="#tags">Tags</a></li>
        </ul>
      </div>
    [[/ignoreTags]]
  </div>
  
    <div class="tab-pane active-pane" id="branches" data-filter-placeholder="Filter branches">
      <ol class="filter-list">
        <li class="empty-msg">No matching branches</li>
        [[#branches]]
          
            [[#hasMultipleHeads]]
              [[#heads]]
                <li class="comprev filter-item">
                  <a class="pjax-trigger filter-item-link" href="/wswp/code/src/[[changeset]]/chapter03/downloader.py?at=[[safeName]]"
                     title="[[name]]">
                    [[name]] ([[shortChangeset]])
                  </a>
                </li>
              [[/heads]]
            [[/hasMultipleHeads]]
            [[^hasMultipleHeads]]
              <li class="comprev filter-item">
                <a class="pjax-trigger filter-item-link" href="/wswp/code/src/[[changeset]]/chapter03/downloader.py?at=[[safeName]]" title="[[name]]">
                  [[name]]
                </a>
              </li>
            [[/hasMultipleHeads]]
          
        [[/branches]]
      </ol>
    </div>
    <div class="tab-pane" id="tags" data-filter-placeholder="Filter tags">
      <ol class="filter-list">
        <li class="empty-msg">No matching tags</li>
        [[#tags]]
          <li class="comprev filter-item">
            <a class="pjax-trigger filter-item-link" href="/wswp/code/src/[[changeset]]/chapter03/downloader.py?at=[[safeName]]" title="[[name]]">
              [[name]]
            </a>
          </li>
        [[/tags]]
      </ol>
    </div>
  
</div>

      </script>
    
      <script id="mention-result" type="text/html">
        
<span class="mention-result">
  <span class="aui-avatar aui-avatar-small mention-result--avatar">
    <span class="aui-avatar-inner">
      <img src="[[avatar_url]]">
    </span>
  </span>
  [[#display_name]]
    <span class="display-name mention-result--display-name">[[&display_name]]</span> <small class="username mention-result--username">[[&username]]</small>
  [[/display_name]]
  [[^display_name]]
    <span class="username mention-result--username">[[&username]]</span>
  [[/display_name]]
  [[#is_teammate]][[^is_team]]
    <span class="aui-lozenge aui-lozenge-complete aui-lozenge-subtle mention-result--lozenge">teammate</span>
  [[/is_team]][[/is_teammate]]
</span>
      </script>
    
      <script id="mention-call-to-action" type="text/html">
        
[[^query]]
<li class="bb-typeahead-item">Begin typing to search for a user</li>
[[/query]]
[[#query]]
<li class="bb-typeahead-item">Continue typing to search for a user</li>
[[/query]]

      </script>
    
      <script id="mention-no-results" type="text/html">
        
[[^searching]]
<li class="bb-typeahead-item">Found no matching users for <em>[[query]]</em>.</li>
[[/searching]]
[[#searching]]
<li class="bb-typeahead-item bb-typeahead-searching">Searching for <em>[[query]]</em>.</li>
[[/searching]]

      </script>
    
      <script id="emoji-result" type="text/html">
        
<div class="aui-avatar aui-avatar-small">
  <div class="aui-avatar-inner">
    <img src="[[src]]">
  </div>
</div>
<span class="name">[[&name]]</span>

      </script>
    
      <script id="repo-typeahead-result" type="text/html">
        <span class="aui-avatar aui-avatar-project aui-avatar-xsmall">
  <span class="aui-avatar-inner">
    <img src="[[avatar]]">
  </span>
</span>
<span class="owner">[[&owner]]</span>/<span class="slug">[[&slug]]</span>

      </script>
    
      <script id="share-form-template" type="text/html">
        

<div class="error aui-message hidden">
  <span class="aui-icon icon-error"></span>
  <div class="message"></div>
</div>
<form class="aui">
  <table class="widget bb-list aui">
    <thead>
    <tr class="assistive">
      <th class="user">User</th>
      <th class="role">Role</th>
      <th class="actions">Actions</th>
    </tr>
    </thead>
    <tbody>
      <tr class="form">
        <td colspan="2">
          <input type="text" class="text bb-user-typeahead user-or-email"
                 placeholder="Username or email address"
                 autocomplete="off"
                 data-bb-typeahead-focus="false"
                 [[#disabled]]disabled[[/disabled]]>
        </td>
        <td class="actions">
          <button type="submit" class="aui-button aui-button-light" disabled>Add</button>
        </td>
      </tr>
    </tbody>
  </table>
</form>

      </script>
    
      <script id="share-detail-template" type="text/html">
        

[[#username]]
<td class="user
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[displayName]]">
    <a href="/[[username]]/" class="user">
      <span class="aui-avatar aui-avatar-xsmall">
        <span class="aui-avatar-inner">
          <img src="[[avatar]]">
        </span>
      </span>
      <span>[[displayName]]</span>
    </a>
  </div>
</td>
[[/username]]
[[^username]]
<td class="email
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[email]]">
    <span class="aui-icon aui-icon-small aui-iconfont-email"></span>
    [[email]]
  </div>
</td>
[[/username]]
<td class="role
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    [[#group]]
      [[#hasCustomGroups]]
        <select class="group [[#noGroupChoices]]hidden[[/noGroupChoices]]">
          [[#groups]]
            <option value="[[slug]]"
                [[#isSelected]]selected[[/isSelected]]>
              [[name]]
            </option>
          [[/groups]]
        </select>
      [[/hasCustomGroups]]
      [[^hasCustomGroups]]
      <label>
        <input type="checkbox" class="admin"
            [[#isAdmin]]checked[[/isAdmin]]>
        Administrator
      </label>
      [[/hasCustomGroups]]
    [[/group]]
    [[^group]]
      <ul>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^read]]aui-lozenge-subtle[[/read]]"
            data-permission="read">
          read
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^write]]aui-lozenge-subtle[[/write]]"
            data-permission="write">
          write
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
            [[^admin]]aui-lozenge-subtle[[/admin]]"
            data-permission="admin">
          admin
        </li>
      </ul>
    [[/group]]
  </div>
</td>
<td class="actions
    [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    <a href="#" class="delete">
      <span class="aui-icon aui-icon-small aui-iconfont-remove">Delete</span>
    </a>
  </div>
</td>

      </script>
    
      <script id="share-team-template" type="text/html">
        

<div class="clearfix">
  <span class="team-avatar-container">
    <span class="aui-avatar aui-avatar-medium">
      <span class="aui-avatar-inner">
        <img src="[[avatar]]">
      </span>
    </span>
  </span>
  <span class="team-name-container">
    [[display_name]]
  </span>
</div>
<p class="helptext">
  
    Existing users are granted access to this team immediately.
    New users will be sent an invitation.
  
</p>
<div class="share-form"></div>

      </script>
    
      <script id="scope-list-template" type="text/html">
        <ul class="scope-list">
  [[#scopes]]
    <li class="scope-list--item">
      <span class="scope-list--icon aui-icon aui-icon-small [[icon]]"></span>
      <span class="scope-list--description">[[description]]</span>
    </li>
  [[/scopes]]
</ul>

      </script>
    
      <script id="source-changeset" type="text/html">
        

<a href="/wswp/code/src/[[raw_node]]/[[path]]?at=default"
    class="[[#selected]]highlight[[/selected]]"
    data-hash="[[node]]">
  [[#author.username]]
    <span class="aui-avatar aui-avatar-xsmall">
      <span class="aui-avatar-inner">
        <img src="[[author.avatar]]">
      </span>
    </span>
    <span class="author" title="[[raw_author]]">[[author.display_name]]</span>
  [[/author.username]]
  [[^author.username]]
    <span class="aui-avatar aui-avatar-xsmall">
      <span class="aui-avatar-inner">
        <img src="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/img/default_avatar/user_blue.svg">
      </span>
    </span>
    <span class="author unmapped" title="[[raw_author]]">[[author]]</span>
  [[/author.username]]
  <time datetime="[[utctimestamp]]" data-title="true">[[utctimestamp]]</time>
  <span class="message">[[message]]</span>
</a>

      </script>
    
      <script id="embed-template" type="text/html">
        

<form class="aui inline-dialog-embed-dialog">
  <label for="embed-code-[[dialogId]]">Embed this source in another page:</label>
  <input type="text" readonly="true" value="&lt;script src=&quot;[[url]]&quot;&gt;&lt;/script&gt;" id="embed-code-[[dialogId]]" class="embed-code">
</form>

      </script>
    
  </div>




  
  


<script src="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/jsi18n/en/djangojs.js"></script>
<script src="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/dist/webpack/vendor.js"></script>
<script src="https://d301sr5gafysq2.cloudfront.net/c4a7121149e9/dist/webpack/app.js"></script>


<script async src="https://www.google-analytics.com/analytics.js"></script>

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","queueTime":0,"licenseKey":"a2cef8c3d3","agent":"","transactionName":"Z11RZxdWW0cEVkYLDV4XdUYLVEFdClsdAAtEWkZQDlJBGgRFQhFMQl1DXFcZQ10AQkFYBFlUVlEXWEJHAA==","applicationID":"1841284","errorBeacon":"bam.nr-data.net","applicationTime":211}</script>
</body>
</html>