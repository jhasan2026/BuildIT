// const post_pic1 = document.getElementById('post_pic1');
// const pic1_filename = document.getElementById('pic1_filename');
// const imagePreview1 = document.getElementById('image-preview1');
//
// // Check if the event listener has been added before
// let isEventListenerAdded = false;
//
// post_pic1.addEventListener('change', (event) => {
//     const file = event.target.files[0];
//
//     if (file) {
//         pic1_filename.textContent = file.name;
//
//         const reader = new FileReader();
//         reader.onload = (e) => {
//             imagePreview1.innerHTML =
//                 `<img src="${e.target.result}" class="max-h-48 rounded-lg mx-auto" alt="Image preview" />`;
//             imagePreview1.classList.remove('border-dashed', 'border-2', 'border-gray-400');
//
//             // Add event listener for image preview only once
//             if (!isEventListenerAdded) {
//                 imagePreview1.addEventListener('click', () => {
//                     post_pic1.click();
//                 });
//
//                 isEventListenerAdded = true;
//             }
//         };
//         reader.readAsDataURL(file);
//     } else {
//         pic1_filename.textContent = '';
//         imagePreview1.innerHTML =
//             `<div class="bg-gray-200 h-48 rounded-lg flex items-center justify-center text-gray-500">No image preview</div>`;
//         imagePreview1.classList.add('border-dashed', 'border-2', 'border-gray-400');
//
//         // Remove the event listener when there's no image
//         imagePreview1.removeEventListener('click', () => {
//             post_pic1.click();
//         });
//
//         isEventListenerAdded = false;
//     }
// });
//
// uploadInput.addEventListener('click', (event) => {
//     event.stopPropagation();
// });

for (let i = 1; i <= 6; i++) {
    const postPic = document.getElementById(`post_pic${i}`);
    const picFilename = document.getElementById(`pic${i}_filename`);
    const imagePreview = document.getElementById(`image-preview${i}`);

    // Check if the event listener has been added before
    let isEventListenerAdded = false;

    postPic.addEventListener('change', (event) => {
        const file = event.target.files[0];

        if (file) {
            picFilename.textContent = file.name;

            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.innerHTML =
                    `<img src="${e.target.result}" class="max-h-48 rounded-lg mx-auto" alt="Image preview" />`;
                imagePreview.classList.remove('border-dashed', 'border-2', 'border-gray-400');

                // Add event listener for image preview only once
                if (!isEventListenerAdded) {
                    imagePreview.addEventListener('click', () => {
                        postPic.click();
                    });

                    isEventListenerAdded = true;
                }
            };
            reader.readAsDataURL(file);
        } else {
            picFilename.textContent = '';
            imagePreview.innerHTML =
                `<div class="bg-gray-200 h-48 rounded-lg flex items-center justify-center text-gray-500">No image preview</div>`;
            imagePreview.classList.add('border-dashed', 'border-2', 'border-gray-400');

            // Remove the event listener when there's no image
            imagePreview.removeEventListener('click', () => {
                postPic.click();
            });

            isEventListenerAdded = false;
        }
    });
}

// Prevent the event from bubbling up for all upload inputs
document.querySelectorAll('.uploadInput').forEach(input => {
    input.addEventListener('click', (event) => {
        event.stopPropagation();
    });
});

