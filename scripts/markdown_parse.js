(function markdownParse(){
	var md_body = document.getElementById("md-body");
	// console.log(md_body.innerText);
	md_body_content = md_body.innerHTML;
	document.body.removeChild(md_body);
	var re = /书名：(.*?)\s/
	var title = re.exec(md_body_content);
	if(title){
		document.getElementsByTagName("title")[0].innerHTML = title[1];		
	}

	var xmp = document.createElement("xmp");
	xmp.setAttribute("theme","united");
	xmp.setAttribute("style","display:block");

	xmp.innerHTML = md_body_content;

	document.body.appendChild(xmp);

	var script_src = document.getElementsByTagName('script')[0].getAttribute('src');
	script_src = script_src.replace("markdown_parse","strapdown");

	var strapdownScript =  document.createElement("script");
	strapdownScript.setAttribute("src",script_src);
	document.body.appendChild(strapdownScript);
})();