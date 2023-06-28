var dbtn = document.getElementById("downloadButton");
var title = document.getElementById("title")
var content = document.getElementById("content")
var download = document.getElementById("download")
var Username=""
// Youtubedownloader
dbtn.addEventListener("click", () => {
    var linkf = document.getElementById("postUrlInput").value;

    var url = "http://127.0.0.1:8000/insta?link=" +linkf
    console.log(url);
    fetch(url, { mode: 'cors', method: "GET" })
        .then((response) => response.json())
        .then((data) => {
            fetch(url, { mode: 'cors', method: "GET" })
                .then((response) => response.json())
                .then((data) => {
                    console.log(data)
            //         content.innerHTML = `
            // <img src="${data.thumb}" id="thumb"></img>
            // <div class='col' >
            // <span id="title">${data.title}</span>
            // <span id="views">Views: ${data.views}</span>
            // <span id="duration">Duration: ${data.duration}</span>
            // <span id="likes">Likes: ${data.likes}</span>       
            // </div>
            // `

            //         download.innerHTML += `
            //     <div class="row">
            //     <a href="/ytd/360p/${data.name + ".mp4"}" download="${data.title}.mp4">360p</a>
            //     <a href="/ytd/480p/${data.name + ".mp4"}" download="${data.title}.mp4">480p</a>
            //     <a href="/ytd/720p/${data.name + ".mp4"}" download="${data.title}.mp4">720p</a>
            //     <a href="/ytd/1080p/${data.name + ".mp4"}" download="${data.title}.mp4">1080p</a>
            //     <a href="/ytd/audio/${data.name + ".mp4"}" download="${data.title}.mp3">Audio</a>
            // </div>
            //     `
                    console.log("Done")

                }


                )
        })
        .catch(error => console.error(error))
    downloadFile(url)
    

})

// download the file
function downloadFile(posturl,type) {
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
      if(type =="video"){
        link.download = 'IGVIDEO.mp4';
      }
      else{
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
function reqdownload(){
  var linkf = document.getElementById("postUrlInputIg").value;
  var url = "http://127.0.0.1:8000/insta?link=" +linkf
  var type="video"
  downloadFile(url,type)
}
// download image
function reqdownloadimg(){
  var linkf = document.getElementById("postUrlInputIg").value;
  var url = "http://127.0.0.1:8000/insta?link=" +linkf
  var type="image"
  downloadFile(url,type)
}

var igdownload=document.getElementById("downloadButtonig")

igdownload.addEventListener("click",()=>{
  var linkf = document.getElementById("postUrlInputIg").value;
  var url = "https://d3a0-2401-4900-1c80-c727-40da-4189-7d12-a8e9.ngrok-free.app/insta?link=" +linkf
  fetch(url, { mode: 'cors', method: "GET" })
        .then((response) => response.json())
        .then((data) => {
           console.log(data)
          //           content.innerHTML = `
          //   <div class='col' >s
          //   <span id="title">Username: ${data.username}</span>
          //   <span id="views">Likes: ${data.likes}</span>
          //   <span id="duration">Type: ${data.type}</span>    
          //   </div>
          //   `
          //   var username=data.username;
          //   if(data.type =="video"){
          //     download.innerHTML = `
          //     <div class="row">
          //     <button onclick="reqdownload()" >Download</button>

          // </div>
          //     `
          //   }
          //   else{
          //     download.innerHTML = `
          //     <div class="row">
          //     <button onclick="reqdownloadimg()" >Download</button>

          // </div>`
          //   }

                    
                    console.log("Done")

                }


                )
        })
        .catch(error => console.error(error))