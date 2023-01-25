window.onload = () => {
	$('INPUT#btn_translate').click(() => {
		let lang = $('INPUT#language_code').val();
		console.log(lang)
		$.get('https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang, (data, textStatus) => {
			if (textStatus === 'success') {
				console.log(data.hello);
			}
		})
	});
}
