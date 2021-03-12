const centangJankas = document.querySelector('.januarikas')
const centangFebkas = document.querySelector('.febuarikas')
const centangMarkas = document.querySelector('.maretkas')
const centangAprkas = document.querySelector('.aprilkas')
const centangMeikas = document.querySelector('.meikas')
const centangJunkas = document.querySelector('.junikas')
const centangJulkas = document.querySelector('.julikas')
const centangAugkas = document.querySelector('.agustuskas')
const centangSepkas = document.querySelector('.septemberkas')
const centangOctkas = document.querySelector('.oktoberkas')
const centangNovkas = document.querySelector('.novemberkas')
const centangDeskas = document.querySelector('.desemberkas')

datakas.forEach(function (d) {
    if ('januari' === d.bulan) {
        centangJankas.removeAttribute('href')
        centangJankas.classList.replace('btn-danger', 'btn-success')
        centangJankas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('febuari' === d.bulan) {
        centangFebkas.removeAttribute('href')
        centangFebkas.classList.replace('btn-danger', 'btn-success')
        centangFebkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('maret' === d.bulan) {
        centangMarkas.removeAttribute('href')
        centangMarkas.classList.replace('btn-danger', 'btn-success')
        centangMarkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('april' === d.bulan) {
        centangAprkas.removeAttribute('href')
        centangAprkas.classList.replace('btn-danger', 'btn-success')
        centangAprkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('mei' === d.bulan) {
        centangMeikas.removeAttribute('href')
        centangMeikas.classList.replace('btn-danger', 'btn-success')
        centangMeikas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('juni' === d.bulan) {
        centangJunkas.removeAttribute('href')
        centangJunkas.classList.replace('btn-danger', 'btn-success')
        centangJunkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('juli' === d.bulan) {
        centangJulkas.removeAttribute('href')
        centangJulkas.classList.replace('btn-danger', 'btn-success')
        centangJulkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('agustus' === d.bulan) {
        centangAugkas.removeAttribute('href')
        centangAugkas.classList.replace('btn-danger', 'btn-success')
        centangAugkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('september' === d.bulan) {
        centangSepkas.removeAttribute('href')
        centangSepkas.classList.replace('btn-danger', 'btn-success')
        centangSepkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('oktober' === d.bulan) {
        centangOctkas.removeAttribute('href')
        centangOctkas.classList.replace('btn-danger', 'btn-success')
        centangOctkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('november' === d.bulan) {
        centangNovkas.removeAttribute('href')
        centangNovkas.classList.replace('btn-danger', 'btn-success')
        centangNovkas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
    if ('desember' === d.bulan) {
        centangDeskas.removeAttribute('href')
        centangDeskas.classList.replace('btn-danger', 'btn-success')
        centangDeskas.firstElementChild.classList.replace('fa-times', 'fa-check')
    }
})

const janClaslistkas = Array.from(centangJankas.classList)
const febClaslistkas = Array.from(centangFebkas.classList)
const marClaslistkas = Array.from(centangMarkas.classList)
const aprClaslistkas = Array.from(centangAprkas.classList)
const meiClaslistkas = Array.from(centangMeikas.classList)
const junClaslistkas = Array.from(centangJunkas.classList)
const julClaslistkas = Array.from(centangJulkas.classList)
const augClaslistkas = Array.from(centangAugkas.classList)
const sepClaslistkas = Array.from(centangSepkas.classList)
const octClaslistkas = Array.from(centangOctkas.classList)
const novClaslistkas = Array.from(centangNovkas.classList)
const desClaslistkas = Array.from(centangDeskas.classList)

if (janClaslistkas.includes('btn-danger')) {
    centangJankas.removeAttribute('href')
    centangJankas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=januari&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (febClaslistkas.includes('btn-danger')) {
    centangFebkas.removeAttribute('href')
    centangFebkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=febuari&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (marClaslistkas.includes('btn-danger')) {
    centangMarkas.removeAttribute('href')
    centangMarkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=maret&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (aprClaslistkas.includes('btn-danger')) {
    centangAprkas.removeAttribute('href')
    centangAprkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=april&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (meiClaslistkas.includes('btn-danger')) {
    centangMeikas.removeAttribute('href')
    centangMeikas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=mei&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (junClaslistkas.includes('btn-danger')) {
    centangJunkas.removeAttribute('href')
    centangJunkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=juni&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (julClaslistkas.includes('btn-danger')) {
    centangJulkas.removeAttribute('href')
    centangJulkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=juli&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (augClaslistkas.includes('btn-danger')) {
    centangAugkas.removeAttribute('href')
    centangAugkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=agustus&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (sepClaslistkas.includes('btn-danger')) {
    centangSepkas.removeAttribute('href')
    centangSepkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=september&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (octClaslistkas.includes('btn-danger')) {
    centangOctkas.removeAttribute('href')
    centangOctkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=oktober&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (novClaslistkas.includes('btn-danger')) {
    centangNovkas.removeAttribute('href')
    centangNovkas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=november&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
if (desClaslistkas.includes('btn-danger')) {
    centangDeskas.removeAttribute('href')
    centangDeskas.setAttribute('href', `${window.origin}/konfirmasi/iurankas?bulan=desember&tahun=${tahundata.value.replace(/\s+/g, '')}`)
}
