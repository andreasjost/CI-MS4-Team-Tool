const startHour = 0
const endHour = 24
const hoursRange = endHour - startHour;
const expandedDayWidth = 300;


$(document).ready(function() {
    weekTables();

    // select a date column to expand
    $('.select-col').click(function() {
        $(this).parent().toggleClass('expand-day');
        $(this).find('div.expand-time').toggleClass('show-timescale');
        $(this).find('div.time-label').remove();
        x = expandedDayWidth / hoursRange; // for the with of the time grid
        
        for (let i = startHour; i < endHour; i++) {
            var el = '<div class="time-label" ' +
                'style="width: ' + x + 'px;">'+ i +
                 '</div>';
            $(this).find('div.expand-time').append(el);
        }
        
    });
});



let calendarLabels = {
    weekDays: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
    allMonths: ["January", "February", "March", "April", "Mai", "June", "July", "August", "September", "October", "November", "December"]
};




function weekTables() {

    let buildingSpace = document.getElementById("weeks-container");
    let today = new Date();
    let loopDate = new Date();
    loopDate.setDate(1);

    let cssGrid = document.createElement('div');
    cssGrid.classList.add('month-table');
    buildingSpace.appendChild(cssGrid);

    
    // build the left column
    let colLeft = document.createElement('div');
    colLeft.classList.add('table-column', 'table-col-fixed');
    cssGrid.appendChild(colLeft);

    let colLeftTitle = document.createElement('div');
    colLeftTitle.classList.add('table-header');
    colLeftTitle.innerHTML = '<br>' + "Name";
    colLeft.appendChild(colLeftTitle);

    for (let i = 0; i < 24; i++) {
        let timeLabel = document.createElement('div');
        timeLabel.classList.add('table-cell');
        timeLabel.innerText = String(i);
        colLeft.appendChild(timeLabel);
    }

    while (loopDate.getMonth() == today.getMonth()) {

        // create a new column
        let dayColumn = document.createElement('div');
        dayColumn.classList.add('table-column');
        cssGrid.appendChild(dayColumn);

        // column header (date)
        let dayColumnHead = document.createElement('div');
        dayColumnHead.classList.add('table-header');
        dayColumnHead.classList.add('select-col'); // reaction to click
        dayColumnHead.innerHTML = '<a href="#!"><span class="hday">' +
            calendarLabels.weekDays[loopDate.getDay()] + '</span>' + loopDate.getDate() + 
            '<div class="expand-time"></div></a>';
        dayColumn.appendChild(dayColumnHead);

        // create all the cells
        for (let i = 0; i < 24; i++) {
            let cell = document.createElement('div');
            cell.classList.add('table-cell');
            if (i % 2 == 0) {
                cell.classList.add('even-row');
            }
            if (loopDate.getDay() == 0) {
                cell.classList.add('neweek-border');
                if (i == 0) {
                    cell.innerText = loopDate.getWeek();
                    cell.classList.add('week-number');
                }
            }
            dayColumn.appendChild(cell);
        }
        loopDate.setDate(loopDate.getDate() + 1); 
    }
    
}



// get the calendarweek-number
Date.prototype.getWeek = function() {
    var onejan = new Date(this.getFullYear(), 0, 1);
    return Math.ceil((((this - onejan) / 86400000) + onejan.getDay() + 1) / 7);
}
