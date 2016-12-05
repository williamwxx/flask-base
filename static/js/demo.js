/**
 * Created by Administrator on 2016/5/23.
 */
    function edit(page_id){
        $("#"+page_id).append('<form action="/blog/edit/" class="edit_input_box">'+
        '<input type="hidden" size="50" name="page_id" class="itembox" value="'+page_id+'">'+
        '<input type="text" size="50" name="page" class="itembox">'+
		'<input type="submit" value="submit" class="edit btn btn-success">'+
	'</form>');
    }
    function done(page_id){
        location.href = "/blog/done/?page_id="+page_id
    }