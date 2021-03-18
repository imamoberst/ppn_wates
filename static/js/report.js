const datepickeryear = document.getElementById('datepickeryear')
const datepickeryearkas = document.getElementById('datepickeryearkas')

datepickeryear.value = tahunreport
datepickeryearkas.value = tahunreport
let dataSemuaIuran = Array.from(JSON.parse(dataiuransemuanya))
let dataIuranFilter = []
let dataKasFilter = []
dataSemuaIuran.filter(e => {
    e.iuran.filter(function (d) {
        if (d.tahun === tahunreport) {
            d.iuranbulanan.forEach(f => dataIuranFilter.push({...f, "norumah": e.norumah}))
            d.iurankas.forEach(f => dataKasFilter.push({...f, "norumah": e.norumah}))
        }
    })
})
dataIuranFilter.forEach(function (e) {
    const aData = document.querySelector(`.iuran-${e.norumah}-${e.bulan}`)
    if (aData) {
        aData.classList.replace('btn-danger', 'btn-success')
        aData.querySelector("i").classList.replace('fa-times', 'fa-check')
    }
})

dataKasFilter.forEach(function (e) {
    const aKas = document.querySelector(`.kas-${e.norumah}-${e.bulan}`)
    if (aKas) {
        aKas.classList.replace('btn-danger', 'btn-success')
        aKas.querySelector("i").classList.replace('fa-times', 'fa-check')
    }
})

