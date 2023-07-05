var title = document.getElementById("title")
var content = document.getElementById("content")
var download = document.getElementById("download")



// download the file
function downloadFile(posturl, type) {
    const fileUrl = posturl; // Replace with the API endpoint URL

    fetch(posturl)
        .then(response => {
            if (response.ok) {
                return response.blob();
            } else {
                throw new Error('Error downloading file.');
            }
        })
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            if (type == "video") {
                link.download = 'IGVIDEO.mp4';
            }
            else {
                link.download = 'IGPOST.png';

            }
            // Specify the desired file name for the downloaded file
            link.click();
            URL.revokeObjectURL(url);
        })
        .catch(error => {
            console.error(error);
        });
}
// download video 
function reqdownload() {
    var linkf = document.getElementById("postUrlInputIg").value;
    var url = "https://freelance-project-ytmp3-production.up.railway.app/insta?link=" + linkf
    var type = "video"
    downloadFile(url, type)
}
// download image
function reqdownloadimg() {
    var linkf = document.getElementById("postUrlInputIg").value;
    var url = "https://freelance-project-ytmp3-production.up.railway.app/insta?link=" + linkf
    var type = "image"
    downloadFile(url, type)
}

var igdownload = document.getElementById("downloadButtonig")
var loader = document.getElementById("loader")

igdownload.addEventListener("click", () => {
    loader.style.display = "flex";
    var linkf = document.getElementById("postUrlInputIg").value;
    var url = "https://freelance-project-ytmp3-production.up.railway.app/insta?link=" + linkf
    fetch(url, { mode: 'cors', method: "GET" })
        .then((response) => response.json())
        .then((data) => {
           


            const videos = data.videourls;
            const images = data.imageurls;
            if (videos.length == 1) {
                loader.style.display = "none";

                content.innerHTML += `
                    <div class="dcard">
                        <div class="profilerr">

                            <img src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile">
                            <span class="pun" >${data.username}</span>
                        </div>
                        <div class="cover">
                            <video src="${videos[0]}" controls ></video>
                        </div>
                        <div class="dowlik">
                            <a href="${videos[0]}">Download Video</a>
                        </div>
                    </div>`
            }
            if (images.length == 1) {
                loader.style.display = "none";

                content.innerHTML += `
                     <div class="dcard">
                    <div class="profilerr">
                        <img src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile">
                        <div class="col">
                                <span class="pun" >${data.username}</span>
                                <span class="pun" >${data.name}</span>
                                    </div>
                    </div>
                    <div class="cover">
                        <img src="${images[0]}" alt="expired">
                    </div>
                    <div class="desc">
                        <span class="pun" >${data.caption}</span>
                    </div>                    
                    <div class="dowlik">
                        <a href="${images[0]}">Download Image</a>
                    </div>
                    </div> 

                `
            }
            if (videos.length > 1) {

                for (let index = 0; index < videos.length; index++) {
                    loader.style.display = "none";

                    content.innerHTML += `
                        <div class="dcard">
                            <div class="profilerr">

                                <img src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile">
                                <div class="col">
                                <span class="pun" >${data.username}</span>
                                <span class="pun" >${data.name}</span>
                                    </div>
                                
                            </div>
                            <div class="cover">
                                <video src="${videos[index]}" controls ></video>
                            </div>
                            <div class="dowlik">
                                <a href="${videos[index]}">Download Video</a>
                            </div>
                        </div> 
`
                }
            }
            if (images.length > 1) {
                for (let index = 0; index < images.length; index++) {
                    loader.style.display = "none";

                    content.innerHTML += `
                    <div class="dcard">
                        <div class="profilerr">
                            <img src="https://cdn-icons-png.flaticon.com/512/3106/3106773.png" alt="profile">
                            <div class="col">
                                <span class="pun" >${data.username}</span>
                                <span class="pun" >${data.name}</span>
                                    </div>
                        </div>
                        <div class="cover">
                            <img src="${images[index]}" alt="expired">
                        </div>
                        <div class="dowlik">
                            <a href="${images[index]}">Download Image</a>
                        </div>
                    </div> 

                `

                }
            }

        }
        
        ).catch(error =>
        content.innerHTML = `<h1>Please check Your URL or Check if the Account is Not PRIVATE</h1>`
    )
})