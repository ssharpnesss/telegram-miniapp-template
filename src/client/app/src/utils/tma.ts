import { backButton, init, initData, miniApp, swipeBehavior, viewport } from "@tma.js/sdk"

const tmaInit = async () => {
  try {
    init();
    initData.restore()

    if (backButton.isSupported()) {
      backButton.mount()
    }
    if (miniApp.isSupported()) {
      miniApp.mount()
      if (miniApp.isMounted()) {
        miniApp.setHeaderColor("#000000")
        miniApp.setBgColor("#000000")
        miniApp.setBottomBarColor("#000000")
      }
    }

    await viewport.mount()
    if (viewport.isMounted()) {
      viewport.expand();
      viewport.bindCssVars();

      const isMobile = /android|iphone|ipad|mobile/i.test(
        navigator.userAgent.toLowerCase(),
      );

      if (isMobile) await viewport.requestFullscreen();
    }

    if (swipeBehavior.isSupported()) {
      swipeBehavior.mount()
      if (swipeBehavior.isMounted()) swipeBehavior.disableVertical()
    }

    miniApp.ready()
    
  } catch (e) {
    console.log("TMA INIT error", e)
  }
}

export {tmaInit};