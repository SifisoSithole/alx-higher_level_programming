window.onload = () => {
	const list = $('UL.my_list');
	$('DIV#add_item').click(() => {
		list.append("<li>Item</li>")
	});
	$('DIV#remove_item').click(() => {
		$('UL.my_list li:last-child').remove();
	});
	$('DIV#clear_list').click(() => {
		list.empty();
	});
}
