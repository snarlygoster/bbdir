// -------------------------------------------------------------------
// markItUp!
// -------------------------------------------------------------------
// Copyright (C) 2008 Jay Salvat
// http://markitup.jaysalvat.com/
// -------------------------------------------------------------------
// MarkDown tags example
// http://en.wikipedia.org/wiki/Markdown
// http://daringfireball.net/projects/markdown/
// -------------------------------------------------------------------
// Feel free to add more tags
// -------------------------------------------------------------------
mySettings = {
	previewParserPath:	'/cgi-bin/django.fcgi/markitup/preview/',
	onShiftEnter:		{keepDefault:false, openWith:'\n\n'},
	markupSet: [
/* 
		{name:'First Level Heading', className:'markItUpButtonH1' key:'1', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
		{name:'Second Level Heading', className:'markItUpButtonH2', key:'2', placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
		{name:'Heading 3', className:'markItUpButtonH3', key:'3', openWith:'### ', placeHolder:'Your title here...' },
		{name:'Heading 4', className:'markItUpButtonH4', key:'4', openWith:'#### ', placeHolder:'Your title here...' },
		{name:'Heading 5', className:'markItUpButtonH5', key:'5', openWith:'##### ', placeHolder:'Your title here...' },
		{name:'Heading 6', className:'markItUpButtonH6', key:'6', openWith:'###### ', placeHolder:'Your title here...' },
		{separator:'---------------' },		
		{name:'Bold', className:'markItUpButtonBold', key:'B', openWith:'**', closeWith:'**'},
		{name:'Italic', className:'markItUpButtonItalic', key:'I', openWith:'_', closeWith:'_'},
		{separator:'---------------' },
		{name:'Bulleted List', className:'markItUpButtonBulletedList', openWith:'- ' },
		{name:'Numeric List', className:'markItUpButtonNumericList', openWith:function(markItUp) {
			return markItUp.line+'. ';
		}},
		{separator:'---------------' },

 */
		{name:'Picture', className:'markItUpButtonPicture', key:'P', replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")'},
		{name:'Link', className:'markItUpButtonLink', key:'L', openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...' },
		{separator:'---------------'},	
		{name:'Quotes', className:'markItUpButtonQuotes' , openWith:'> '},
		{name:'Code Block / Code', className:'markItUpButtonCode', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)'},
		{separator:'---------------'},
		{name:'Preview', call:'preview', className:"markItUpButtonPreview"},
		{name:'Insert footnote', className:"markItUpButtonFootnote",
			beforeInsert: function(h) {
				instructions = "Type in the number of the footnote:)";
				if (!h.last_footnote) {
				h.last_footnote = prompt(instructions);
				} else {
					if (!isNaN(h.last_footnote))
						h.last_footnote = parseInt(h.last_footnote) +1;
					else
						h.last_footnote = prompt(instructions);
				}
				h.footnote_content = prompt("Type in the text of the footnote:");
			},
			closeWith: function(h) {
				return '[^' + h.last_footnote + ']';
			},
			afterInsert: function(h) {
				h.textarea.value += '[^' + h.last_footnote + ']: ' +
				h.footnote_content;
			}},
	]
}

// mIu nameSpace to avoid conflict.
miu = {
	markdownTitle: function(markItUp, char) {
		heading = '';
		n = $.trim(markItUp.selection||markItUp.placeHolder).length;
		// work around bug in python-markdown where header underlines must be at least 3 chars
		if (n < 3) { n = 3; }
		for(i = 0; i < n; i++) {
			heading += char;
		}
		return '\n'+heading;
	}
}
