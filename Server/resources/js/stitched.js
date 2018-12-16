/*
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

//Authors: Noah Zeilmann

'use-strict'
$(document).ready(function() {
	let buttonA = $('#buttonA'),
		buttonB = $('#buttonB'),
		overlay = $('#overlay'),
		magSelect = $("#mag-select");


	$('.pannable-image').ImageViewer();
	overlay.addClass('d-none');

	buttonA.click(function(e) {
		window.location.replace(LOCATION_A+"?magLevel="+magSelect.val());
	});

	buttonB.click(function(e) {
		window.location.replace(LOCATION_B+"?magLevel="+magSelect.val());
	});
});