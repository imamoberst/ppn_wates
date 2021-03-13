let dataBulan = []
const inputBulan = document.getElementById('databulan')
const tCheck = document.querySelectorAll('.form-check-input')
tCheck.forEach(function (e) {
    e.addEventListener('click', function (e) {
        if (this.checked) {
            let bulan = e.target.value
            dataBulan.push(bulan)
            inputBulan.value = dataBulan
        } else {
            let bulan = e.target.value
            dataBulan = dataBulan.filter(e => e !== bulan)
            inputBulan.value = dataBulan
        }
    })
})