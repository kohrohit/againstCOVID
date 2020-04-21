
#SERVER_URL = "https://drf.ert.com/"
SERVER_URL = "https://staging.ert.com/"
# SERVER_URL = "0.0.0.0:8000/"

master_email_reciever = [
    "customercare@ert.com",
]

proforma_invoice_mail = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Respmail is a response HTML email designed to work on all major email platforms and smartphones</title>
		<style type="text/css">
			/* RESET STYLES */
			html {{ background-color:#E1E1E1; margin:0; padding:0; }}
			body, #bodyTable, #bodyCell, #bodyCell{{height:100% !important; margin:0; padding:0; width:100% !important;font-family:Helvetica, Arial, "Lucida Grande", sans-serif;}}
			table{{border-collapse:collapse;}}
			table[id=bodyTable] {{width:100%!important;margin:auto;max-width:500px!important;color:#7A7A7A;font-weight:normal;}}
			img, a img{{border:0; outline:none; text-decoration:none;height:auto; line-height:100%;}}
			a {{text-decoration:none !important;border-bottom: 1px solid;}}
			h1, h2, h3, h4, h5, h6{{color:#5F5F5F; font-weight:normal; font-family:Helvetica; font-size:20px; line-height:125%; text-align:Left; letter-spacing:normal;margin-top:0;margin-right:0;margin-bottom:10px;margin-left:0;padding-top:0;padding-bottom:0;padding-left:0;padding-right:0;}}

			/* CLIENT-SPECIFIC STYLES */
			.ReadMsgBody{{width:100%;}} .ExternalClass{{width:100%;}} /* Force Hotmail/Outlook.com to display emails at full width. */
			.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div{{line-height:100%;}} /* Force Hotmail/Outlook.com to display line heights normally. */
			table, td{{mso-table-lspace:0pt; mso-table-rspace:0pt;}} /* Remove spacing between tables in Outlook 2007 and up. */
			#outlook a{{padding:0;}} /* Force Outlook 2007 and up to provide a "view in browser" message. */
			img{{-ms-interpolation-mode: bicubic;display:block;outline:none; text-decoration:none;}} /* Force IE to smoothly render resized images. */
			body, table, td, p, a, li, blockquote{{-ms-text-size-adjust:100%; -webkit-text-size-adjust:100%; font-weight:normal !important;}} /* Prevent Windows- and Webkit-based mobile platforms from changing declared text sizes. */
			.ExternalClass td[class="ecxflexibleContainerBox"] h3 {{padding-top: 10px !important;}} /* Force hotmail to push 2-grid sub headers down */

			/* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

			/* ========== Page Styles ========== */
			h1{{display:block;font-size:26px;font-style:normal;font-weight:normal;line-height:100%;}}
			h2{{display:block;font-size:20px;font-style:normal;font-weight:normal;line-height:120%;}}
			h3{{display:block;font-size:17px;font-style:normal;font-weight:normal;line-height:110%;}}
			h4{{display:block;font-size:18px;font-style:italic;font-weight:normal;line-height:100%;}}
			.flexibleImage{{height:auto;}}
			.linkRemoveBorder{{border-bottom:0 !important;}}
			table[class=flexibleContainerCellDivider] {{padding-bottom:0 !important;padding-top:0 !important;}}

			body, #bodyTable{{background-color:#E1E1E1;}}
			#emailHeader{{background-color:#E1E1E1;}}
			#emailBody{{background-color:#FFFFFF;}}
			#emailFooter{{background-color:#E1E1E1;}}
			.nestedContainer{{background-color:#F8F8F8; border:1px solid #CCCCCC;}}
			.emailButton{{background-color:#205478; border-collapse:separate;}}
			.buttonContent{{color:#FFFFFF; font-family:Helvetica; font-size:18px; font-weight:bold; line-height:100%; padding:15px; text-align:center;}}
			.buttonContent a{{color:#FFFFFF; display:block; text-decoration:none !important; border:0 !important;}}
			.emailCalendar{{background-color:#FFFFFF; border:1px solid #CCCCCC;}}
			.emailCalendarMonth{{background-color:#205478; color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; padding-top:10px; padding-bottom:10px; text-align:center;}}
			.emailCalendarDay{{color:#205478; font-family:Helvetica, Arial, sans-serif; font-size:60px; font-weight:bold; line-height:100%; padding-top:20px; padding-bottom:20px; text-align:center;}}
			.imageContentText {{margin-top: 10px;line-height:0;}}
			.imageContentText a {{line-height:0;}}
			#invisibleIntroduction {{display:none !important;}} /* Removing the introduction text from the view */

			/*FRAMEWORK HACKS & OVERRIDES */
			span[class=ios-color-hack] a {{color:#275100 !important;text-decoration:none !important;}} /* Remove all link colors in IOS (below are duplicates based on the color preference) */
			span[class=ios-color-hack2] a {{color:#205478 !important;text-decoration:none !important;}}
			span[class=ios-color-hack3] a {{color:#8B8B8B !important;text-decoration:none !important;}}
			/* A nice and clean way to target phone numbers you want clickable and avoid a mobile phone from linking other numbers that look like, but are not phone numbers.  Use these two blocks of code to "unstyle" any numbers that may be linked.  The second block gives you a class to apply with a span tag to the numbers you would like linked and styled.
			Inspired by Campaign Monitor's article on using phone numbers in email: http://www.campaignmonitor.com/blog/post/3571/using-phone-numbers-in-html-email/.
			*/
			.a[href^="tel"], a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:none !important;cursor:default !important;}}
			.mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:auto !important;cursor:default !important;}}


			/* MOBILE STYLES */
			@media only screen and (max-width: 480px){{
				/*////// CLIENT-SPECIFIC STYLES //////*/
				body{{width:100% !important; min-width:100% !important;}} /* Force iOS Mail to render the email at full width. */

				/* FRAMEWORK STYLES */
				/*
				CSS selectors are written in attribute
				selector format to prevent Yahoo Mail
				from rendering media query styles on
				desktop.
				*/
				/*td[class="textContent"], td[class="flexibleContainerCell"] {{ width: 100%; padding-left: 10px !important; padding-right: 10px !important; }}*/
				table[id="emailHeader"],
				table[id="emailBody"],
				table[id="emailFooter"],
				table[class="flexibleContainer"],
				td[class="flexibleContainerCell"] {{width:100% !important;}}
				td[class="flexibleContainerBox"], td[class="flexibleContainerBox"] table {{display: block;width: 100%;text-align: left;}}
				/*
				The following style rule makes any
				image classed with 'flexibleImage'
				fluid when the query activates.
				Make sure you add an inline max-width
				to those images to prevent them
				from blowing out.
				*/
				td[class="imageContent"] img {{height:auto !important; width:100% !important; max-width:100% !important; }}
				img[class="flexibleImage"]{{height:auto !important; width:100% !important;max-width:100% !important;}}
				img[class="flexibleImageSmall"]{{height:auto !important; width:auto !important;}}


				/*
				Create top space for every second element in a block
				*/
				table[class="flexibleContainerBoxNext"]{{padding-top: 10px !important;}}

				/*
				Make buttons in the email span the
				full width of their container, allowing
				for left- or right-handed ease of use.
				*/
				table[class="emailButton"]{{width:100% !important;}}
				td[class="buttonContent"]{{padding:0 !important;}}
				td[class="buttonContent"] a{{padding:15px !important;}}

			}}

			/*  CONDITIONS FOR ANDROID DEVICES ONLY
			*   http://developer.android.com/guide/webapps/targeting.html
			*   http://pugetworks.com/2011/04/css-media-queries-for-targeting-different-mobile-devices/ ;
			=====================================================*/

			@media only screen and (-webkit-device-pixel-ratio:.75){{
				/* Put CSS for low density (ldpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1){{
				/* Put CSS for medium density (mdpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1.5){{
				/* Put CSS for high density (hdpi) Android layouts in here */
			}}
			/* end Android targeting */

			/* CONDITIONS FOR IOS DEVICES ONLY
			=====================================================*/
			@media only screen and (min-device-width : 320px) and (max-device-width:568px) {{

			}}
			/* end IOS targeting */
		</style>
		<!--
			Outlook Conditional CSS

			These two style blocks target Outlook 2007 & 2010 specifically, forcing
			columns into a single vertical stack as on mobile clients. This is
			primarily done to avoid the 'page break bug' and is optional.

			More information here:
			http://templates.mailchimp.com/development/css/outlook-conditional-css
		-->
		<!--[if mso 12]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
		<!--[if mso 14]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
	</head>
	<body bgcolor="#E1E1E1" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">

		<!-- CENTER THE EMAIL // -->
		<!--
		1.  The center tag should normally put all the
			content in the middle of the email page.
			I added "table-layout: fixed;" style to force
			yahoomail which by default put the content left.

		2.  For hotmail and yahoomail, the contents of
			the email starts from this center, so we try to
			apply necessary styling e.g. background-color.
		-->
		<center style="background-color:#E1E1E1;">
			<table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="table-layout: fixed;max-width:100% !important;width: 100% !important;min-width: 100% !important;">
				<tr>
					<td align="center" valign="top" id="bodyCell">

						<!-- EMAIL HEADER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailHeader">

							<!-- HEADER ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="10" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td valign="top" width="500" class="flexibleContainerCell">

															<!-- CONTENT TABLE // -->
															<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
																<tr>

																	<td align="left" valign="middle" id="invisibleIntroduction" class="flexibleContainerBox" style="display:none !important; mso-hide:all;">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																	<td align="right" valign="middle" class="flexibleContainerBox">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<!-- CONTENT // -->
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->

						</table>
						<!-- // END -->

						<!-- EMAIL BODY // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#FFFFFF"  border="0" cellpadding="0" cellspacing="0" width="500" id="emailBody">

							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="#F8F8F8">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" align="center"  style="text-align:center;" class="textContent">
																					<!--
																						The "mc:edit" is a feature for MailChimp which allows
																						you to edit certain row. It makes it easy for you to quickly edit row sections.
																						http://kb.mailchimp.com/templates/code/create-editable-content-areas-with-mailchimps-template-language
																					-->
																					<h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:center;"><img src="https://app.ert.com/static/img/tax_invoice.png" alt=""/></h3>
																					<div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->


                            <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->




							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="30" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td style="padding-top:0;" align="center" valign="top" width="500" class="flexibleContainerCell">

															<!-- CONTENT TABLE // -->
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                                <tr>
                                                                    <td valign="top" class="textContent">
                                                                        <!--
                                                                            The "mc:edit" is a feature for MailChimp which allows
                                                                            you to edit certain row. It makes it easy for you to quickly edit row sections.
                                                                            http://kb.mailchimp.com/templates/code/create-editable-content-areas-with-mailchimps-template-language
                                                                        -->
                                                                        <h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;">Hello {member[0]},</h3>
                                                                        <div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">Kindly Check Proforma Invoice Detials<br>

																			Partner Name: {partner[0]} <br>
																			Quantity: {quantity[0]} <br>
																			Rate: {rate[0]} <br>
																			City: {city[0]} <br>
																			Tax Amount: {tax_amount[0]} <br>
																			Grand Total: {grand_total_amount[0]} <br>
																			Delivery Charges: {delivery_charges[0]} <br>

																			From ERT India. Regards.<br><br>Team ERT </div>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                            <!-- // CONTENT TABLE -->

														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

                            <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">This is an machine-generated email. Please do not reply. </div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->
                            <!-- MODULE DIVIDER // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->


							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
                                                                                    <div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Contact Us: <a href="mailto:info@ert.com">info@ert.com</a> or Call us <a href="tel:+919922919009">919922919009</a></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

						</table>
						<!-- // END -->

						<!-- EMAIL FOOTER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailFooter">

							<!-- FOOTER ROW // -->
							<!--
								To move or duplicate any of the design patterns
								in this email, simply move or copy the entire
								MODULE ROW section for each content block.
							-->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td valign="top" bgcolor="#E1E1E1">

																		<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
																			<div>Copyright &#169; 2020 <a href="https://app.ert.com/easydiesel/member" target="_blank" style="text-decoration:none;color:#828282;"><span style="color:#828282;">ERT India Private Limited.</span></a> All rights reserved.</div>
																			<div></div>
																		</div>

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>

						</table>
						<!-- // END -->

					</td>
				</tr>
			</table>
		</center>
	</body>
</html>

'''


report_issue_mail = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Respmail is a response HTML email designed to work on all major email platforms and smartphones</title>
		<style type="text/css">
			/* RESET STYLES */
			html {{ background-color:#E1E1E1; margin:0; padding:0; }}
			body, #bodyTable, #bodyCell, #bodyCell{{height:100% !important; margin:0; padding:0; width:100% !important;font-family:Helvetica, Arial, "Lucida Grande", sans-serif;}}
			table{{border-collapse:collapse;}}
			table[id=bodyTable] {{width:100%!important;margin:auto;max-width:500px!important;color:#7A7A7A;font-weight:normal;}}
			img, a img{{border:0; outline:none; text-decoration:none;height:auto; line-height:100%;}}
			a {{text-decoration:none !important;border-bottom: 1px solid;}}
			h1, h2, h3, h4, h5, h6{{color:#5F5F5F; font-weight:normal; font-family:Helvetica; font-size:20px; line-height:125%; text-align:Left; letter-spacing:normal;margin-top:0;margin-right:0;margin-bottom:10px;margin-left:0;padding-top:0;padding-bottom:0;padding-left:0;padding-right:0;}}

			/* CLIENT-SPECIFIC STYLES */
			.ReadMsgBody{{width:100%;}} .ExternalClass{{width:100%;}} /* Force Hotmail/Outlook.com to display emails at full width. */
			.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div{{line-height:100%;}} /* Force Hotmail/Outlook.com to display line heights normally. */
			table, td{{mso-table-lspace:0pt; mso-table-rspace:0pt;}} /* Remove spacing between tables in Outlook 2007 and up. */
			#outlook a{{padding:0;}} /* Force Outlook 2007 and up to provide a "view in browser" message. */
			img{{-ms-interpolation-mode: bicubic;display:block;outline:none; text-decoration:none;}} /* Force IE to smoothly render resized images. */
			body, table, td, p, a, li, blockquote{{-ms-text-size-adjust:100%; -webkit-text-size-adjust:100%; font-weight:normal !important;}} /* Prevent Windows- and Webkit-based mobile platforms from changing declared text sizes. */
			.ExternalClass td[class="ecxflexibleContainerBox"] h3 {{padding-top: 10px !important;}} /* Force hotmail to push 2-grid sub headers down */

			/* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

			/* ========== Page Styles ========== */
			h1{{display:block;font-size:26px;font-style:normal;font-weight:normal;line-height:100%;}}
			h2{{display:block;font-size:20px;font-style:normal;font-weight:normal;line-height:120%;}}
			h3{{display:block;font-size:17px;font-style:normal;font-weight:normal;line-height:110%;}}
			h4{{display:block;font-size:18px;font-style:italic;font-weight:normal;line-height:100%;}}
			.flexibleImage{{height:auto;}}
			.linkRemoveBorder{{border-bottom:0 !important;}}
			table[class=flexibleContainerCellDivider] {{padding-bottom:0 !important;padding-top:0 !important;}}

			body, #bodyTable{{background-color:#E1E1E1;}}
			#emailHeader{{background-color:#E1E1E1;}}
			#emailBody{{background-color:#FFFFFF;}}
			#emailFooter{{background-color:#E1E1E1;}}
			.nestedContainer{{background-color:#F8F8F8; border:1px solid #CCCCCC;}}
			.emailButton{{background-color:#205478; border-collapse:separate;}}
			.buttonContent{{color:#FFFFFF; font-family:Helvetica; font-size:18px; font-weight:bold; line-height:100%; padding:15px; text-align:center;}}
			.buttonContent a{{color:#FFFFFF; display:block; text-decoration:none !important; border:0 !important;}}
			.emailCalendar{{background-color:#FFFFFF; border:1px solid #CCCCCC;}}
			.emailCalendarMonth{{background-color:#205478; color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; padding-top:10px; padding-bottom:10px; text-align:center;}}
			.emailCalendarDay{{color:#205478; font-family:Helvetica, Arial, sans-serif; font-size:60px; font-weight:bold; line-height:100%; padding-top:20px; padding-bottom:20px; text-align:center;}}
			.imageContentText {{margin-top: 10px;line-height:0;}}
			.imageContentText a {{line-height:0;}}
			#invisibleIntroduction {{display:none !important;}} /* Removing the introduction text from the view */

			/*FRAMEWORK HACKS & OVERRIDES */
			span[class=ios-color-hack] a {{color:#275100 !important;text-decoration:none !important;}} /* Remove all link colors in IOS (below are duplicates based on the color preference) */
			span[class=ios-color-hack2] a {{color:#205478 !important;text-decoration:none !important;}}
			span[class=ios-color-hack3] a {{color:#8B8B8B !important;text-decoration:none !important;}}
			/* A nice and clean way to target phone numbers you want clickable and avoid a mobile phone from linking other numbers that look like, but are not phone numbers.  Use these two blocks of code to "unstyle" any numbers that may be linked.  The second block gives you a class to apply with a span tag to the numbers you would like linked and styled.
			Inspired by Campaign Monitor's article on using phone numbers in email: http://www.campaignmonitor.com/blog/post/3571/using-phone-numbers-in-html-email/.
			*/
			.a[href^="tel"], a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:none !important;cursor:default !important;}}
			.mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:auto !important;cursor:default !important;}}


			/* MOBILE STYLES */
			@media only screen and (max-width: 480px){{
				/*////// CLIENT-SPECIFIC STYLES //////*/
				body{{width:100% !important; min-width:100% !important;}} /* Force iOS Mail to render the email at full width. */

				/* FRAMEWORK STYLES */
				/*
				CSS selectors are written in attribute
				selector format to prevent Yahoo Mail
				from rendering media query styles on
				desktop.
				*/
				/*td[class="textContent"], td[class="flexibleContainerCell"] {{ width: 100%; padding-left: 10px !important; padding-right: 10px !important; }}*/
				table[id="emailHeader"],
				table[id="emailBody"],
				table[id="emailFooter"],
				table[class="flexibleContainer"],
				td[class="flexibleContainerCell"] {{width:100% !important;}}
				td[class="flexibleContainerBox"], td[class="flexibleContainerBox"] table {{display: block;width: 100%;text-align: left;}}
				/*
				The following style rule makes any
				image classed with 'flexibleImage'
				fluid when the query activates.
				Make sure you add an inline max-width
				to those images to prevent them
				from blowing out.
				*/
				td[class="imageContent"] img {{height:auto !important; width:100% !important; max-width:100% !important; }}
				img[class="flexibleImage"]{{height:auto !important; width:100% !important;max-width:100% !important;}}
				img[class="flexibleImageSmall"]{{height:auto !important; width:auto !important;}}


				/*
				Create top space for every second element in a block
				*/
				table[class="flexibleContainerBoxNext"]{{padding-top: 10px !important;}}

				/*
				Make buttons in the email span the
				full width of their container, allowing
				for left- or right-handed ease of use.
				*/
				table[class="emailButton"]{{width:100% !important;}}
				td[class="buttonContent"]{{padding:0 !important;}}
				td[class="buttonContent"] a{{padding:15px !important;}}

			}}

			/*  CONDITIONS FOR ANDROID DEVICES ONLY
			*   http://developer.android.com/guide/webapps/targeting.html
			*   http://pugetworks.com/2011/04/css-media-queries-for-targeting-different-mobile-devices/ ;
			=====================================================*/

			@media only screen and (-webkit-device-pixel-ratio:.75){{
				/* Put CSS for low density (ldpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1){{
				/* Put CSS for medium density (mdpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1.5){{
				/* Put CSS for high density (hdpi) Android layouts in here */
			}}
			/* end Android targeting */

			/* CONDITIONS FOR IOS DEVICES ONLY
			=====================================================*/
			@media only screen and (min-device-width : 320px) and (max-device-width:568px) {{

			}}
			/* end IOS targeting */
		</style>
		<!--
			Outlook Conditional CSS

			These two style blocks target Outlook 2007 & 2010 specifically, forcing
			columns into a single vertical stack as on mobile clients. This is
			primarily done to avoid the 'page break bug' and is optional.

			More information here:
			http://templates.mailchimp.com/development/css/outlook-conditional-css
		-->
		<!--[if mso 12]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
		<!--[if mso 14]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
	</head>
	<body bgcolor="#E1E1E1" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">

		<!-- CENTER THE EMAIL // -->
		<!--
		1.  The center tag should normally put all the
			content in the middle of the email page.
			I added "table-layout: fixed;" style to force
			yahoomail which by default put the content left.

		2.  For hotmail and yahoomail, the contents of
			the email starts from this center, so we try to
			apply necessary styling e.g. background-color.
		-->
		<center style="background-color:#E1E1E1;">
			<table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="table-layout: fixed;max-width:100% !important;width: 100% !important;min-width: 100% !important;">
				<tr>
					<td align="center" valign="top" id="bodyCell">

						<!-- EMAIL HEADER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailHeader">

							<!-- HEADER ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="10" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td valign="top" width="500" class="flexibleContainerCell">

															<!-- CONTENT TABLE // -->
															<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
																<tr>

																	<td align="left" valign="middle" id="invisibleIntroduction" class="flexibleContainerBox" style="display:none !important; mso-hide:all;">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																	<td align="right" valign="middle" class="flexibleContainerBox">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<!-- CONTENT // -->
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->

						</table>
						<!-- // END -->

						<!-- EMAIL BODY // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#FFFFFF"  border="0" cellpadding="0" cellspacing="0" width="500" id="emailBody">

							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="#F8F8F8">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" align="center"  style="text-align:center;" class="textContent">
																					<!--
																						The "mc:edit" is a feature for MailChimp which allows
																						you to edit certain row. It makes it easy for you to quickly edit row sections.
																						http://kb.mailchimp.com/templates/code/create-editable-content-areas-with-mailchimps-template-language
																					-->
																					<h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:center;"><img src="https://app.ert.com/static/img/tax_invoice.png" alt=""/></h3>
																					<div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->


                            <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->




							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="30" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td style="padding-top:0;" align="center" valign="top" width="500" class="flexibleContainerCell">

															<!-- CONTENT TABLE // -->
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                                <tr>
                                                                    <td valign="top" class="textContent">
                                                                        <!--
                                                                            The "mc:edit" is a feature for MailChimp which allows
                                                                            you to edit certain row. It makes it easy for you to quickly edit row sections.
                                                                            http://kb.mailchimp.com/templates/code/create-editable-content-areas-with-mailchimps-template-language
                                                                        -->
                                                                        <h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;">Hello {member_name},</h3>
                                                                        <div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">

																		<h4 style="font-weight:bold;"> Issue: </h4> {issue} <br>
																		<h4 style="font-weight:bold;"> Issue Description:</h4> {issue_description} <br>
																			

																			From ERT India. Regards.<br><br>Team ERT </div>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                            <!-- // CONTENT TABLE -->

														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

                            <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">This is an machine-generated email. Please do not reply. </div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->
                            <!-- MODULE DIVIDER // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->


							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
                                                                                    <div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Contact Us: <a href="mailto:info@ert.com">info@ert.com</a> or Call us <a href="tel:+919922919009">919922919009</a></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

						</table>
						<!-- // END -->

						<!-- EMAIL FOOTER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailFooter">

							<!-- FOOTER ROW // -->
							<!--
								To move or duplicate any of the design patterns
								in this email, simply move or copy the entire
								MODULE ROW section for each content block.
							-->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td valign="top" bgcolor="#E1E1E1">

																		<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
																			<div>Copyright &#169; 2020 <a href="https://app.ert.com/easydiesel/member" target="_blank" style="text-decoration:none;color:#828282;"><span style="color:#828282;">ERT India Private Limited.</span></a> All rights reserved.</div>
																			<div></div>
																		</div>

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>

						</table>
						<!-- // END -->

					</td>
				</tr>
			</table>
		</center>
	</body>
</html>

'''


forgot_password_email = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Respmail is a response HTML email designed to work on all major email platforms and smartphones</title>
		<style type="text/css">
			/* RESET STYLES */
			html {{ background-color:#E1E1E1; margin:0; padding:0; }}
			body, #bodyTable, #bodyCell, #bodyCell{{height:100% !important; margin:0; padding:0; width:100% !important;font-family:Helvetica, Arial, "Lucida Grande", sans-serif;}}
			table{{border-collapse:collapse;}}
			table[id=bodyTable] {{width:100%!important;margin:auto;max-width:500px!important;color:#7A7A7A;font-weight:normal;}}
			img, a img{{border:0; outline:none; text-decoration:none;height:auto; line-height:100%;}}
			a {{text-decoration:none !important;border-bottom: 1px solid;}}
			h1, h2, h3, h4, h5, h6{{color:#5F5F5F; font-weight:normal; font-family:Helvetica; font-size:20px; line-height:125%; text-align:Left; letter-spacing:normal;margin-top:0;margin-right:0;margin-bottom:10px;margin-left:0;padding-top:0;padding-bottom:0;padding-left:0;padding-right:0;}}

			/* CLIENT-SPECIFIC STYLES */
			.ReadMsgBody{{width:100%;}} .ExternalClass{{width:100%;}} /* Force Hotmail/Outlook.com to display emails at full width. */
			.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div{{line-height:100%;}} /* Force Hotmail/Outlook.com to display line heights normally. */
			table, td{{mso-table-lspace:0pt; mso-table-rspace:0pt;}} /* Remove spacing between tables in Outlook 2007 and up. */
			#outlook a{{padding:0;}} /* Force Outlook 2007 and up to provide a "view in browser" message. */
			img{{-ms-interpolation-mode: bicubic;display:block;outline:none; text-decoration:none;}} /* Force IE to smoothly render resized images. */
			body, table, td, p, a, li, blockquote{{-ms-text-size-adjust:100%; -webkit-text-size-adjust:100%; font-weight:normal!important;}} /* Prevent Windows- and Webkit-based mobile platforms from changing declared text sizes. */
			.ExternalClass td[class="ecxflexibleContainerBox"] h3 {{padding-top: 10px !important;}} /* Force hotmail to push 2-grid sub headers down */

			/* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

			/* ========== Page Styles ========== */
			h1{{display:block;font-size:26px;font-style:normal;font-weight:normal;line-height:100%;}}
			h2{{display:block;font-size:20px;font-style:normal;font-weight:normal;line-height:120%;}}
			h3{{display:block;font-size:17px;font-style:normal;font-weight:normal;line-height:110%;}}
			h4{{display:block;font-size:18px;font-style:italic;font-weight:normal;line-height:100%;}}
			.flexibleImage{{height:auto;}}
			.linkRemoveBorder{{border-bottom:0 !important;}}
			table[class=flexibleContainerCellDivider] {{padding-bottom:0 !important;padding-top:0 !important;}}

			body, #bodyTable{{background-color:#E1E1E1;}}
			#emailHeader{{background-color:#E1E1E1;}}
			#emailBody{{background-color:#FFFFFF;}}
			#emailFooter{{background-color:#E1E1E1;}}
			.nestedContainer{{background-color:#F8F8F8; border:1px solid #CCCCCC;}}
			.emailButton{{background-color:#205478; border-collapse:separate;}}
			.buttonContent{{color:#FFFFFF; font-family:Helvetica; font-size:18px; font-weight:bold; line-height:100%; padding:15px; text-align:center;}}
			.buttonContent a{{color:#FFFFFF; display:block; text-decoration:none!important; border:0!important;}}
			.emailCalendar{{background-color:#FFFFFF; border:1px solid #CCCCCC;}}
			.emailCalendarMonth{{background-color:#205478; color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; padding-top:10px; padding-bottom:10px; text-align:center;}}
			.emailCalendarDay{{color:#205478; font-family:Helvetica, Arial, sans-serif; font-size:60px; font-weight:bold; line-height:100%; padding-top:20px; padding-bottom:20px; text-align:center;}}
			.imageContentText {{margin-top: 10px;line-height:0;}}
			.imageContentText a {{line-height:0;}}
			#invisibleIntroduction {{display:none !important;}} /* Removing the introduction text from the view */

			/*FRAMEWORK HACKS & OVERRIDES */
			span[class=ios-color-hack] a {{color:#275100!important;text-decoration:none!important;}} /* Remove all link colors in IOS (below are duplicates based on the color preference) */
			span[class=ios-color-hack2] a {{color:#205478!important;text-decoration:none!important;}}
			span[class=ios-color-hack3] a {{color:#8B8B8B!important;text-decoration:none!important;}}
			/* A nice and clean way to target phone numbers you want clickable and avoid a mobile phone from linking other numbers that look like, but are not phone numbers.  Use these two blocks of code to "unstyle" any numbers that may be linked.  The second block gives you a class to apply with a span tag to the numbers you would like linked and styled.
			Inspired by Campaign Monitor's article on using phone numbers in email: http://www.campaignmonitor.com/blog/post/3571/using-phone-numbers-in-html-email/.
			*/
			.a[href^="tel"], a[href^="sms"] {{text-decoration:none!important;color:#606060!important;pointer-events:none!important;cursor:default!important;}}
			.mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {{text-decoration:none!important;color:#606060!important;pointer-events:auto!important;cursor:default!important;}}


			/* MOBILE STYLES */
			@media only screen and (max-width: 480px){{
				/*////// CLIENT-SPECIFIC STYLES //////*/
				body{{width:100% !important; min-width:100% !important;}} /* Force iOS Mail to render the email at full width. */

				/* FRAMEWORK STYLES */
				/*
				CSS selectors are written in attribute
				selector format to prevent Yahoo Mail
				from rendering media query styles on
				desktop.
				*/
				/*td[class="textContent"], td[class="flexibleContainerCell"] {{ width: 100%; padding-left: 10px !important; padding-right: 10px !important; }}*/
				table[id="emailHeader"],
				table[id="emailBody"],
				table[id="emailFooter"],
				table[class="flexibleContainer"],
				td[class="flexibleContainerCell"] {{width:100% !important;}}
				td[class="flexibleContainerBox"], td[class="flexibleContainerBox"] table {{display: block;width: 100%;text-align: left;}}
				/*
				The following style rule makes any
				image classed with 'flexibleImage'
				fluid when the query activates.
				Make sure you add an inline max-width
				to those images to prevent them
				from blowing out.
				*/
				td[class="imageContent"] img {{height:auto !important; width:100% !important; max-width:100% !important; }}
				img[class="flexibleImage"]{{height:auto !important; width:100% !important;max-width:100% !important;}}
				img[class="flexibleImageSmall"]{{height:auto !important; width:auto !important;}}


				/*
				Create top space for every second element in a block
				*/
				table[class="flexibleContainerBoxNext"]{{padding-top: 10px !important;}}

				/*
				Make buttons in the email span the
				full width of their container, allowing
				for left- or right-handed ease of use.
				*/
				table[class="emailButton"]{{width:100% !important;}}
				td[class="buttonContent"]{{padding:0 !important;}}
				td[class="buttonContent"] a{{padding:15px !important;}}

			}}

			/*  CONDITIONS FOR ANDROID DEVICES ONLY
			*   http://developer.android.com/guide/webapps/targeting.html
			*   http://pugetworks.com/2011/04/css-media-queries-for-targeting-different-mobile-devices/ ;
			=====================================================*/

			@media only screen and (-webkit-device-pixel-ratio:.75){{
				/* Put CSS for low density (ldpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1){{
				/* Put CSS for medium density (mdpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1.5){{
				/* Put CSS for high density (hdpi) Android layouts in here */
			}}
			/* end Android targeting */

			/* CONDITIONS FOR IOS DEVICES ONLY
			=====================================================*/
			@media only screen and (min-device-width : 320px) and (max-device-width:568px) {{

			}}
			/* end IOS targeting */
		</style>
		<!--
			Outlook Conditional CSS

			These two style blocks target Outlook 2007 & 2010 specifically, forcing
			columns into a single vertical stack as on mobile clients. This is
			primarily done to avoid the 'page break bug' and is optional.

			More information here:
			http://templates.mailchimp.com/development/css/outlook-conditional-css
		-->
		<!--[if mso 12]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
		<!--[if mso 14]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
	</head>
	<body bgcolor="#E1E1E1" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">

		<!-- CENTER THE EMAIL // -->
		<!--
		1.  The center tag should normally put all the
			content in the middle of the email page.
			I added "table-layout: fixed;" style to force
			yahoomail which by default put the content left.

		2.  For hotmail and yahoomail, the contents of
			the email starts from this center, so we try to
			apply necessary styling e.g. background-color.
		-->
		<center style="background-color:#E1E1E1;">
			<table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="table-layout: fixed;max-width:100% !important;width: 100% !important;min-width: 100% !important;">
				<tr>
					<td align="center" valign="top" id="bodyCell">

						<!-- EMAIL HEADER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailHeader">

							<!-- HEADER ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="10" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td valign="top" width="500" class="flexibleContainerCell">

															<!-- CONTENT TABLE // -->
															<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
																<tr>

																	<td align="left" valign="middle" id="invisibleIntroduction" class="flexibleContainerBox" style="display:none !important; mso-hide:all;">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																	<td align="right" valign="middle" class="flexibleContainerBox">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<!-- CONTENT // -->
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->

						</table>
						<!-- // END -->

						<!-- EMAIL BODY // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#FFFFFF"  border="0" cellpadding="0" cellspacing="0" width="500" id="emailBody">









							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="#F8F8F8">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" align="center"  style="text-align:center;" class="textContent">
																					<!--
																						The "mc:edit" is a feature for MailChimp which allows
																						you to edit certain row. It makes it easy for you to quickly edit row sections.
																						http://kb.mailchimp.com/templates/code/create-editable-content-areas-with-mailchimps-template-language
																					-->
																					<h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:center;"><img src="https://app.ert.com/static/img/logo_tans_small.png" alt="" style="height: 100px" /></h3>															
																					<div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->





                           <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">**** Forgot Password Mail ****</div>
																				</td>
																			</tr>

																		</table>
																		<!-- // CONTENT TABLE -->
                                                                        <!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->



                             <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h5 style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;">Hello {name}</h5>
																				</td>
																			</tr>
                                                                            <tr>
																				<td valign="top" class="textContent">
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Your Reset URL is {reset_url}</div>
																				</td>
																			</tr>

																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

							<!-- MODULE ROW // -->
							<!--  The "mc:hideable" is a feature for MailChimp which allows
								you to disable certain row. It works perfectly for our row structure.
								http://kb.mailchimp.com/article/template-language-creating-editable-content-areas/
							-->
							
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Happy ordering #ERT. Please contact ERT in case of any queries. </div>
																				</td>
																			</tr>
                                                                            <tr>
																				<td valign="top" class="textContent">
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Website: <a href="http://www.ert.com" target="_blank">http://www.ert.com</a></div>
																				</td>
																			</tr>

																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

                            <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:100%;">Regards,</div>
                                                                                    <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:100%;">ERT</div>
																				</td>
																			</tr>
																																						
																		</table>
																		<!-- // CONTENT TABLE -->
																		<img  src="http://app.ert.com/static/img/footer.png" alt="" style="width: 100%;margin-top:3px;" />
																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->
                            <!-- MODULE DIVIDER // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->


							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
                                                                                    <div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Contact Us: <a href="mailto:info@ert.com">info@ert.com</a> or Call us <a href="tel:+919922919009">919922919009</a></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

						</table>
						<!-- // END -->

						<!-- EMAIL FOOTER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailFooter">

							<!-- FOOTER ROW // -->
							<!--
								To move or duplicate any of the design patterns
								in this email, simply move or copy the entire
								MODULE ROW section for each content block.
							-->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td valign="top" bgcolor="#E1E1E1">

																		<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
																			<div>Copyright &#169; 2020 <a href="https://app.ert.com/easydiesel/member" target="_blank" style="text-decoration:none;color:#828282;"><span style="color:#828282;">ERT @ drscan.org</span></a> All rights reserved</div>
																			<div></div>
																		</div>

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>

						</table>
						<!-- // END -->

					</td>
				</tr>
			</table>
		</center>
	</body>
</html>


'''


invoice_mail = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Respmail is a response HTML email designed to work on all major email platforms and smartphones</title>
		<style type="text/css">
			/* RESET STYLES */
			html {{ background-color:#E1E1E1; margin:0; padding:0; }}
			body, #bodyTable, #bodyCell, #bodyCell{{height:100% !important; margin:0; padding:0; width:100% !important;font-family:Helvetica, Arial, "Lucida Grande", sans-serif;}}
			table{{border-collapse:collapse;}}
			table[id=bodyTable] {{width:100%!important;margin:auto;max-width:500px!important;color:#7A7A7A;font-weight:normal;}}
			img, a img{{border:0; outline:none; text-decoration:none;height:auto; line-height:100%;}}
			a {{text-decoration:none !important;border-bottom: 1px solid;}}
			h1, h2, h3, h4, h5, h6{{color:#5F5F5F; font-weight:normal; font-family:Helvetica; font-size:20px; line-height:125%; text-align:Left; letter-spacing:normal;margin-top:0;margin-right:0;margin-bottom:10px;margin-left:0;padding-top:0;padding-bottom:0;padding-left:0;padding-right:0;}}

			/* CLIENT-SPECIFIC STYLES */
			.ReadMsgBody{{width:100%;}} .ExternalClass{{width:100%;}} /* Force Hotmail/Outlook.com to display emails at full width. */
			.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div{{line-height:100%;}} /* Force Hotmail/Outlook.com to display line heights normally. */
			table, td{{mso-table-lspace:0pt; mso-table-rspace:0pt;}} /* Remove spacing between tables in Outlook 2007 and up. */
			#outlook a{{padding:0;}} /* Force Outlook 2007 and up to provide a "view in browser" message. */
			img{{-ms-interpolation-mode: bicubic;display:block;outline:none; text-decoration:none;}} /* Force IE to smoothly render resized images. */
			body, table, td, p, a, li, blockquote{{-ms-text-size-adjust:100%; -webkit-text-size-adjust:100%; font-weight:normal !important;}} /* Prevent Windows- and Webkit-based mobile platforms from changing declared text sizes. */
			.ExternalClass td[class="ecxflexibleContainerBox"] h3 {{padding-top: 10px !important;}} /* Force hotmail to push 2-grid sub headers down */

			/* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

			/* ========== Page Styles ========== */
			h1{{display:block;font-size:26px;font-style:normal;font-weight:normal;line-height:100%;}}
			h2{{display:block;font-size:20px;font-style:normal;font-weight:normal;line-height:120%;}}
			h3{{display:block;font-size:17px;font-style:normal;font-weight:normal;line-height:110%;}}
			h4{{display:block;font-size:18px;font-style:italic;font-weight:normal;line-height:100%;}}
			.flexibleImage{{height:auto;}}
			.linkRemoveBorder{{border-bottom:0 !important;}}
			table[class=flexibleContainerCellDivider] {{padding-bottom:0 !important;padding-top:0 !important;}}

			body, #bodyTable{{background-color:#E1E1E1;}}
			#emailHeader{{background-color:#E1E1E1;}}
			#emailBody{{background-color:#FFFFFF;}}
			#emailFooter{{background-color:#E1E1E1;}}
			.nestedContainer{{background-color:#F8F8F8; border:1px solid #CCCCCC;}}
			.emailButton{{background-color:#205478; border-collapse:separate;}}
			.buttonContent{{color:#FFFFFF; font-family:Helvetica; font-size:18px; font-weight:bold; line-height:100%; padding:15px; text-align:center;}}
			.buttonContent a{{color:#FFFFFF; display:block; text-decoration:none !important; border:0 !important;}}
			.emailCalendar{{background-color:#FFFFFF; border:1px solid #CCCCCC;}}
			.emailCalendarMonth{{background-color:#205478; color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; padding-top:10px; padding-bottom:10px; text-align:center;}}
			.emailCalendarDay{{color:#205478; font-family:Helvetica, Arial, sans-serif; font-size:60px; font-weight:bold; line-height:100%; padding-top:20px; padding-bottom:20px; text-align:center;}}
			.imageContentText {{margin-top: 10px;line-height:0;}}
			.imageContentText a {{line-height:0;}}
			#invisibleIntroduction {{display:none !important;}} /* Removing the introduction text from the view */

			/*FRAMEWORK HACKS & OVERRIDES */
			span[class=ios-color-hack] a {{color:#275100 !important;text-decoration:none !important;}} /* Remove all link colors in IOS (below are duplicates based on the color preference) */
			span[class=ios-color-hack2] a {{color:#205478 !important;text-decoration:none !important;}}
			span[class=ios-color-hack3] a {{color:#8B8B8B !important;text-decoration:none !important;}}
			/* A nice and clean way to target phone numbers you want clickable and avoid a mobile phone from linking other numbers that look like, but are not phone numbers.  Use these two blocks of code to "unstyle" any numbers that may be linked.  The second block gives you a class to apply with a span tag to the numbers you would like linked and styled.
			Inspired by Campaign Monitor's article on using phone numbers in email: http://www.campaignmonitor.com/blog/post/3571/using-phone-numbers-in-html-email/.
			*/
			.a[href^="tel"], a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:none !important;cursor:default !important;}}
			.mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:auto !important;cursor:default !important;}}


			/* MOBILE STYLES */
			@media only screen and (max-width: 480px){{
				/*////// CLIENT-SPECIFIC STYLES //////*/
				body{{width:100% !important; min-width:100% !important;}} /* Force iOS Mail to render the email at full width. */

				/* FRAMEWORK STYLES */
				/*
				CSS selectors are written in attribute
				selector format to prevent Yahoo Mail
				from rendering media query styles on
				desktop.
				*/
				/*td[class="textContent"], td[class="flexibleContainerCell"] {{ width: 100%; padding-left: 10px !important; padding-right: 10px !important; }}*/
				table[id="emailHeader"],
				table[id="emailBody"],
				table[id="emailFooter"],
				table[class="flexibleContainer"],
				td[class="flexibleContainerCell"] {{width:100% !important;}}
				td[class="flexibleContainerBox"], td[class="flexibleContainerBox"] table {{display: block;width: 100%;text-align: left;}}
				/*
				The following style rule makes any
				image classed with 'flexibleImage'
				fluid when the query activates.
				Make sure you add an inline max-width
				to those images to prevent them
				from blowing out.
				*/
				td[class="imageContent"] img {{height:auto !important; width:100% !important; max-width:100% !important; }}
				img[class="flexibleImage"]{{height:auto !important; width:100% !important;max-width:100% !important;}}
				img[class="flexibleImageSmall"]{{height:auto !important; width:auto !important;}}


				/*
				Create top space for every second element in a block
				*/
				table[class="flexibleContainerBoxNext"]{{padding-top: 10px !important;}}

				/*
				Make buttons in the email span the
				full width of their container, allowing
				for left- or right-handed ease of use.
				*/
				table[class="emailButton"]{{width:100% !important;}}
				td[class="buttonContent"]{{padding:0 !important;}}
				td[class="buttonContent"] a{{padding:15px !important;}}

			}}

			/*  CONDITIONS FOR ANDROID DEVICES ONLY
			*   http://developer.android.com/guide/webapps/targeting.html
			*   http://pugetworks.com/2011/04/css-media-queries-for-targeting-different-mobile-devices/ ;
			=====================================================*/

			@media only screen and (-webkit-device-pixel-ratio:.75){{
				/* Put CSS for low density (ldpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1){{
				/* Put CSS for medium density (mdpi) Android layouts in here */
			}}

			@media only screen and (-webkit-device-pixel-ratio:1.5){{
				/* Put CSS for high density (hdpi) Android layouts in here */
			}}
			/* end Android targeting */

			/* CONDITIONS FOR IOS DEVICES ONLY
			=====================================================*/
			@media only screen and (min-device-width : 320px) and (max-device-width:568px) {{

			}}
			/* end IOS targeting */
		</style>
		<!--
			Outlook Conditional CSS

			These two style blocks target Outlook 2007 & 2010 specifically, forcing
			columns into a single vertical stack as on mobile clients. This is
			primarily done to avoid the 'page break bug' and is optional.

			More information here:
			http://templates.mailchimp.com/development/css/outlook-conditional-css
		-->
		<!--[if mso 12]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
		<!--[if mso 14]>
			<style type="text/css">
				.flexibleContainer{{display:block !important; width:100% !important;}}
			</style>
		<![endif]-->
	</head>
	<body bgcolor="#E1E1E1" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">

		<!-- CENTER THE EMAIL // -->
		<!--
		1.  The center tag should normally put all the
			content in the middle of the email page.
			I added "table-layout: fixed;" style to force
			yahoomail which by default put the content left.

		2.  For hotmail and yahoomail, the contents of
			the email starts from this center, so we try to
			apply necessary styling e.g. background-color.
		-->
		<center style="background-color:#E1E1E1;">
			<table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="table-layout: fixed;max-width:100% !important;width: 100% !important;min-width: 100% !important;">
				<tr>
					<td align="center" valign="top" id="bodyCell">

						<!-- EMAIL HEADER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailHeader">

							<!-- HEADER ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="10" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td valign="top" width="500" class="flexibleContainerCell">

															<!-- CONTENT TABLE // -->
															<table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
																<tr>

																	<td align="left" valign="middle" id="invisibleIntroduction" class="flexibleContainerBox" style="display:none !important; mso-hide:all;">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																	<td align="right" valign="middle" class="flexibleContainerBox">
																		<table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
																			<tr>
																				<td align="left" class="textContent">
																					<!-- CONTENT // -->
																					<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

																					</div>
																				</td>
																			</tr>
																		</table>
																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->

						</table>
						<!-- // END -->

						<!-- EMAIL BODY // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#FFFFFF"  border="0" cellpadding="0" cellspacing="0" width="500" id="emailBody">

							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%" bgcolor="#F8F8F8">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" align="center"  style="text-align:center;" class="textContent">
																					<!--
																						The "mc:edit" is a feature for MailChimp which allows
																						you to edit certain row. It makes it easy for you to quickly edit row sections.
																						http://kb.mailchimp.com/templates/code/create-editable-content-areas-with-mailchimps-template-language
																					-->
																					<h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:center;"><img src="https://app.ert.com/static/img/tax_invoice.png" alt=""/></h3>
																					<div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->


                            <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;"></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->




							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="30" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td style="padding-top:0;" align="center" valign="top" width="500" class="flexibleContainerCell">

															<!-- CONTENT TABLE // -->
                                                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                                                <tr>
                                                                    <td valign="top" class="textContent">
                                                                        <!--
                                                                            The "mc:edit" is a feature for MailChimp which allows
                                                                            you to edit certain row. It makes it easy for you to quickly edit row sections.
                                                                            http://kb.mailchimp.com/templates/code/create-editable-content-areas-with-mailchimps-template-language
                                                                        -->
                                                                        <h3 mc:edit="header" style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;">Hello {member_name},</h3><br>
                                                                        <div mc:edit="body" style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;color:#5F5F5F;line-height:135%;">Kindly Check Invoice Detials<br>
																			Fuel Delivered From: {partner_name} <br>
																			Order Number: {order_id} <br>
																			Rate: {rate} <br>
																		    Quantity: {quantity} <br>
																			Payment Mode: {payment} <br>
																			Delivered Charges: {delivery_charges} <br>
																			Collected Amount: {collected_amount} <br>		
																			Total Amount: {total_amount} <br><br>		
																			From ERT India. Regards.<br><br>Team ERT </div>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                            <!-- // CONTENT TABLE -->

														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

                            <!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
																					<h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
																					<div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">This is an machine-generated email. Please do not reply. </div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->
                            <!-- MODULE DIVIDER // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // END -->


							<!-- MODULE ROW // -->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td align="center" valign="top">

																		<!-- CONTENT TABLE // -->
																		<table border="0" cellpadding="0" cellspacing="0" width="100%">
																			<tr>
																				<td valign="top" class="textContent">
                                                                                    <div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Contact Us: <a href="mailto:info@ert.com">info@ert.com</a> or Call us <a href="tel:+919922919009">919922919009</a></div>
																				</td>
																			</tr>
																		</table>
																		<!-- // CONTENT TABLE -->

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>
							<!-- // MODULE ROW -->

						</table>
						<!-- // END -->

						<!-- EMAIL FOOTER // -->
						<!--
							The table "emailBody" is the email's container.
							Its width can be set to 100% for a color band
							that spans the width of the page.
						-->
						<table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailFooter">

							<!-- FOOTER ROW // -->
							<!--
								To move or duplicate any of the design patterns
								in this email, simply move or copy the entire
								MODULE ROW section for each content block.
							-->
							<tr>
								<td align="center" valign="top">
									<!-- CENTERING TABLE // -->
									<table border="0" cellpadding="0" cellspacing="0" width="100%">
										<tr>
											<td align="center" valign="top">
												<!-- FLEXIBLE CONTAINER // -->
												<table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
													<tr>
														<td align="center" valign="top" width="500" class="flexibleContainerCell">
															<table border="0" cellpadding="30" cellspacing="0" width="100%">
																<tr>
																	<td valign="top" bgcolor="#E1E1E1">

																		<div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
																			<div>Copyright &#169; 2020 <a href="https://staging-cu.ert.com" target="_blank" style="text-decoration:none;color:#828282;"><span style="color:#828282;">ERT India Private Limited.</span></a> All rights reserved.</div>
																			<div></div>
																		</div>

																	</td>
																</tr>
															</table>
														</td>
													</tr>
												</table>
												<!-- // FLEXIBLE CONTAINER -->
											</td>
										</tr>
									</table>
									<!-- // CENTERING TABLE -->
								</td>
							</tr>

						</table>
						<!-- // END -->

					</td>
				</tr>
			</table>
		</center>
	</body>
</html>

'''


proforma_invoice_mail_v2 = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Respmail is a response HTML email designed to work on all major email platforms and smartphones</title>
    <style type="text/css">
      /* RESET STYLES */
      html {{ background-color:#E1E1E1; margin:0; padding:0; }}
      body, #bodyTable, #bodyCell, #bodyCell{{height:100% !important; margin:0; padding:0; width:100% !important;font-family:Helvetica, Arial, "Lucida Grande", sans-serif;}}
      table{{border-collapse:collapse;}}
      table[id=bodyTable] {{width:100%!important;margin:auto;max-width:500px!important;color:#7A7A7A;font-weight:normal;}}
      img, a img{{border:0; outline:none; text-decoration:none;height:auto; line-height:100%;}}
      a {{text-decoration:none !important;border-bottom: 1px solid;}}
      h1, h2, h3, h4, h5, h6{{color:#5F5F5F; font-weight:normal; font-family:Helvetica; font-size:20px; line-height:125%; text-align:Left; letter-spacing:normal;margin-top:0;margin-right:0;margin-bottom:10px;margin-left:0;padding-top:0;padding-bottom:0;padding-left:0;padding-right:0;}}

      /* CLIENT-SPECIFIC STYLES */
      .ReadMsgBody{{width:100%;}} .ExternalClass{{width:100%;}} /* Force Hotmail/Outlook.com to display emails at full width. */
      .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div{{line-height:100%;}} /* Force Hotmail/Outlook.com to display line heights normally. */
      table, td{{mso-table-lspace:0pt; mso-table-rspace:0pt;}} /* Remove spacing between tables in Outlook 2007 and up. */
      #outlook a{{padding:0;}} /* Force Outlook 2007 and up to provide a "view in browser" message. */
      img{{-ms-interpolation-mode: bicubic;display:block;outline:none; text-decoration:none;}} /* Force IE to smoothly render resized images. */
      body, table, td, p, a, li, blockquote{{-ms-text-size-adjust:100%; -webkit-text-size-adjust:100%; font-weight:normal !important;}} /* Prevent Windows- and Webkit-based mobile platforms from changing declared text sizes. */
      .ExternalClass td[class="ecxflexibleContainerBox"] h3 {{padding-top: 10px !important;}} /* Force hotmail to push 2-grid sub headers down */

      /* /\/\/\/\/\/\/\/\/ TEMPLATE STYLES /\/\/\/\/\/\/\/\/ */

      /* ========== Page Styles ========== */
      h1{{display:block;font-size:26px;font-style:normal;font-weight:normal;line-height:100%;}}
      h2{{display:block;font-size:20px;font-style:normal;font-weight:normal;line-height:120%;}}
      h3{{display:block;font-size:17px;font-style:normal;font-weight:normal;line-height:110%;}}
      h4{{display:block;font-size:18px;font-style:italic;font-weight:normal;line-height:100%;}}
      .flexibleImage{{height:auto;}}
      .linkRemoveBorder{{border-bottom:0 !important;}}
      table[class=flexibleContainerCellDivider] {{padding-bottom:0 !important;padding-top:0 !important;}}

      body, #bodyTable{{background-color:#E1E1E1;}}
      #emailHeader{{background-color:#E1E1E1;}}
      #emailBody{{background-color:#FFFFFF;}}
      #emailFooter{{background-color:#E1E1E1;}}
      .nestedContainer{{background-color:#F8F8F8; border:1px solid #CCCCCC;}}
      .emailButton{{background-color:#205478; border-collapse:separate;}}
      .buttonContent{{color:#FFFFFF; font-family:Helvetica; font-size:18px; font-weight:bold; line-height:100%; padding:15px; text-align:center;}}
      .buttonContent a{{color:#FFFFFF; display:block; text-decoration:none !important; border:0 !important;}}
      .emailCalendar{{background-color:#FFFFFF; border:1px solid #CCCCCC;}}
      .emailCalendarMonth{{background-color:#205478; color:#FFFFFF; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; padding-top:10px; padding-bottom:10px; text-align:center;}}
      .emailCalendarDay{{color:#205478; font-family:Helvetica, Arial, sans-serif; font-size:60px; font-weight:bold; line-height:100%; padding-top:20px; padding-bottom:20px; text-align:center;}}
      .imageContentText {{margin-top: 10px;line-height:0;}}
      .imageContentText a {{line-height:0;}}
      #invisibleIntroduction {{display:none !important;}} /* Removing the introduction text from the view */

      /*FRAMEWORK HACKS & OVERRIDES */
      span[class=ios-color-hack] a {{color:#275100 !important;text-decoration:none !important;}} /* Remove all link colors in IOS (below are duplicates based on the color preference) */
      span[class=ios-color-hack2] a {{color:#205478 !important;text-decoration:none !important;}}
      span[class=ios-color-hack3] a {{color:#8B8B8B !important;text-decoration:none !important;}}
      /* A nice and clean way to target phone numbers you want clickable and avoid a mobile phone from linking other numbers that look like, but are not phone numbers.  Use these two blocks of code to "unstyle" any numbers that may be linked.  The second block gives you a class to apply with a span tag to the numbers you would like linked and styled.
      Inspired by Campaign Monitor's article on using phone numbers in email: http://www.campaignmonitor.com/blog/post/3571/using-phone-numbers-in-html-email/.
      */
      .a[href^="tel"], a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:none !important;cursor:default !important;}}
      .mobile_link a[href^="tel"], .mobile_link a[href^="sms"] {{text-decoration:none !important;color:#606060 !important;pointer-events:auto !important;cursor:default !important;}}


      /* MOBILE STYLES */
      @media only screen and (max-width: 480px){{
        /*////// CLIENT-SPECIFIC STYLES //////*/
        body{{width:100% !important; min-width:100% !important;}} /* Force iOS Mail to render the email at full width. */

        /* FRAMEWORK STYLES */
        /*
        CSS selectors are written in attribute
        selector format to prevent Yahoo Mail
        from rendering media query styles on
        desktop.
        */
        /*td[class="textContent"], td[class="flexibleContainerCell"] {{ width: 100%; padding-left: 10px !important; padding-right: 10px !important; }}*/
        table[id="emailHeader"],
        table[id="emailBody"],
        table[id="emailFooter"],
        table[class="flexibleContainer"],
        td[class="flexibleContainerCell"] {{width:100% !important;}}
        td[class="flexibleContainerBox"], td[class="flexibleContainerBox"] table {{display: block;width: 100%;text-align: left;}}
        /*
        The following style rule makes any
        image classed with 'flexibleImage'
        fluid when the query activates.
        Make sure you add an inline max-width
        to those images to prevent them
        from blowing out.
        */
        td[class="imageContent"] img {{height:auto !important; width:100% !important; max-width:100% !important; }}
        img[class="flexibleImage"]{{height:auto !important; width:100% !important;max-width:100% !important;}}
        img[class="flexibleImageSmall"]{{height:auto !important; width:auto !important;}}


        /*
        Create top space for every second element in a block
        */
        table[class="flexibleContainerBoxNext"]{{padding-top: 10px !important;}}

        /*
        Make buttons in the email span the
        full width of their container, allowing
        for left- or right-handed ease of use.
        */
        table[class="emailButton"]{{width:100% !important;}}
        td[class="buttonContent"]{{padding:0 !important;}}
        td[class="buttonContent"] a{{padding:15px !important;}}

      }}

      /*  CONDITIONS FOR ANDROID DEVICES ONLY
      *   http://developer.android.com/guide/webapps/targeting.html
      *   http://pugetworks.com/2011/04/css-media-queries-for-targeting-different-mobile-devices/ ;
      =====================================================*/

      @media only screen and (-webkit-device-pixel-ratio:.75){{
        /* Put CSS for low density (ldpi) Android layouts in here */
      }}

      @media only screen and (-webkit-device-pixel-ratio:1){{
        /* Put CSS for medium density (mdpi) Android layouts in here */
      }}

      @media only screen and (-webkit-device-pixel-ratio:1.5){{
        /* Put CSS for high density (hdpi) Android layouts in here */
      }}
      /* end Android targeting */

      /* CONDITIONS FOR IOS DEVICES ONLY
      =====================================================*/
      @media only screen and (min-device-width : 320px) and (max-device-width:568px) {{

      }}
      /* end IOS targeting */
    </style>
    <!--
      Outlook Conditional CSS

      These two style blocks target Outlook 2007 & 2010 specifically, forcing
      columns into a single vertical stack as on mobile clients. This is
      primarily done to avoid the 'page break bug' and is optional.

      More information here:
      http://templates.mailchimp.com/development/css/outlook-conditional-css
    -->
    <!--[if mso 12]>
      <style type="text/css">
        .flexibleContainer{{display:block !important; width:100% !important;}}
      </style>
    <![endif]-->
    <!--[if mso 14]>
      <style type="text/css">
        .flexibleContainer{{display:block !important; width:100% !important;}}
      </style>
    <![endif]-->
  </head>
  <body bgcolor="#E1E1E1" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">

    <!-- CENTER THE EMAIL // -->
    <!--
    1.  The center tag should normally put all the
      content in the middle of the email page.
      I added "table-layout: fixed;" style to force
      yahoomail which by default put the content left.

    2.  For hotmail and yahoomail, the contents of
      the email starts from this center, so we try to
      apply necessary styling e.g. background-color.
    -->
    <center style="background-color:#E1E1E1;">
      <table border="0" cellpadding="0" cellspacing="0" height="100%" width="100%" id="bodyTable" style="table-layout: fixed;max-width:100% !important;width: 100% !important;min-width: 100% !important;">
        <tr>
          <td align="center" valign="top" id="bodyCell">

            <!-- EMAIL HEADER // -->
            <!--
              The table "emailBody" is the email's container.
              Its width can be set to 100% for a color band
              that spans the width of the page.
            -->
            <table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailHeader">

              <!-- HEADER ROW // -->
              <tr>
                <td align="center" valign="top">
                  <!-- CENTERING TABLE // -->
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <!-- FLEXIBLE CONTAINER // -->
                        <table border="0" cellpadding="10" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td valign="top" width="500" class="flexibleContainerCell">

                              <!-- CONTENT TABLE // -->
                              <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>

                                  <td align="left" valign="middle" id="invisibleIntroduction" class="flexibleContainerBox" style="display:none !important; mso-hide:all;">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
                                      <tr>
                                        <td align="left" class="textContent">
                                          <div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

                                          </div>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                  <td align="right" valign="middle" class="flexibleContainerBox">
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:100%;">
                                      <tr>
                                        <td align="left" class="textContent">
                                          <!-- CONTENT // -->
                                          <div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">

                                          </div>
                                        </td>
                                      </tr>
                                    </table>
                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <!-- // FLEXIBLE CONTAINER -->
                      </td>
                    </tr>
                  </table>
                  <!-- // CENTERING TABLE -->
                </td>
              </tr>
              <!-- // END -->

            </table>
            <!-- // END -->

            <!-- EMAIL BODY // -->
            <!--
              The table "emailBody" is the email's container.
              Its width can be set to 100% for a color band
              that spans the width of the page.
            -->
            <table bgcolor="#FFFFFF"  border="0" cellpadding="0" cellspacing="0" width="700" id="emailBody">

                            <!-- MODULE ROW // -->
              <tr>
                <td align="center" valign="top">
                  <!-- CENTERING TABLE // -->
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <!-- FLEXIBLE CONTAINER // -->
                        <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td align="center" valign="top" width="500" class="flexibleContainerCell">
                              <table border="0" cellpadding="30" cellspacing="0" width="100%">
                                <tr>
                                  <td align="center" valign="top">

                                    <!-- CONTENT TABLE // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                      <tr>
                                        <td valign="top" class="textContent">
                                          <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:center;">PROFORMA INVOICE</h3>
                                          <div style="text-align:left;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;"></div>
                                        </td>
                                      </tr>
                                    </table>
                                    <!-- // CONTENT TABLE -->

                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <!-- // FLEXIBLE CONTAINER -->
                      </td>
                    </tr>
                  </table>
                  <!-- // CENTERING TABLE -->
                </td>
              </tr>
              <!-- // MODULE ROW -->




              <!-- MODULE ROW // -->
              <tr>
                <td align="center" valign="top">
                  <!-- CENTERING TABLE // -->
                  <table border="0" cellpadding="0" cellspacing="0" width="90%">
                    <tr>
                      <td align="center" valign="top">
                        <!-- FLEXIBLE CONTAINER // -->
                        <table border="1" cellpadding="30" cellspacing="0" width="100%" class="flexibleContainer" style="table-layout: fixed">
                          <tr>
                            <td style="padding-top:5%;" align="center" colspan="6"  >
                              ERT <br>
                            103, KUMAR VASTU , OPPOSITE SYMPHONY HOTEL<br>
                              BHOSALE NAGAR 411020
                            </td>
                          </tr>

                          <tr>
                            <td style="padding-top:0; word-wrap: break-word;" align="left" valign="top"   class="flexibleContainerCell" colspan="3">
                             <b>To</b> {asset_address}
                            </td>
                            <td style="padding-top:0;" align="left" valign="top"  class="flexibleContainerCell" colspan="3">
                              <b>Bill no:</b> N/A <br>
                              <b>Date:</b> {today_date} <br>
                              <b>Po Date:</b> N/A<br>
                            </td>
                          </tr>

                          <tr>
                            <td style="padding-top:0;" align="left" valign="top"  class="flexibleContainerCell" colspan="2">
                              <b>LRNo </b>: N.A
                            </td>
                            <td style="padding-top:0;" align="left" valign="top"  class="flexibleContainerCell" colspan="2">
                              <b>LoadingTime </b>: N.A
                            </td>
                            <td style="padding-top:0;" align="left" valign="top"  class="flexibleContainerCell" colspan="2">
                              <b>SealNo </b>: N.A
                            </td>
                          </tr>

                          <tr>
                            <td style="padding-top:0;" align="left" valign="top"  class="flexibleContainerCell" colspan="3">
                              <b>DriverName </b>: N.A
                            </td>
                            <td style="padding-top:0;" align="left" valign="top"  class="flexibleContainerCell" colspan="3">
                              <b>VehicleNo </b>: N.A
                            </td>

                          </tr>


                          <tr>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              <b>Sr.no</b>
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              <b>Particulars</b>
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              <b>Quantity</b>
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              <b>Unit</b>
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              <b>Rate</b>
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              <b>Amount</b>
                            </td>
                          </tr>

                           <tr>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              1
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              DIESEL
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              {quantity[0]}
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              ltrs
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              {rate[0]}
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1">
                              {grand_total_amount}
                            </td>
                          </tr>

                          <tr>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="4">
                            {inr_to_words}
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1" rowspan="2">
                              <p><b>Sub Total</b></p>
                              <p><b>Con. Fees</b></p>
                              <p><b>GST(18%)</b></p>
                              <p><b>Grand Total</b></p>
                            </td>
                            <td style="padding-top:0;" align="center" valign="top"  class="flexibleContainerCell" colspan="1" rowspan="2">
                              <p>{sub_total[0]}</p><br>
                              <p>{delivery_charges[0]}</p>
                              <p>{tax_amount[0]}</p>
                              <p>{grand_total_amount}</p>
                            </td>
                          </tr>

                          <tr>
                            <td style="padding-top:0;word-wrap: break-word;" class="flexibleContainerCell" colspan="4">
                              <b>Note 1.All payments should be made by RTGS/DD payable in PUNE only.<br/>
                              2.If paid other than on a Pune bank credit will be given for then amount after deduction of the usual bank charges.<br/>
                              3.Interest @ 24% p.a will be debited to your ale if bill is not paid within 7 days of the date of bill.</b>
                            </td>
                          </tr>

                          <tr>
                            <td style="padding-top:0;padding-bottom:0;word-wrap: break-word;" valign="top"  class="flexibleContainerCell" colspan="4" rowspan="2">
                              <b>I/We hereby certify that my/our registration certificate under the Maharashtra Value Added Tax Act,2002 is in force on the date on which the sale of the goods specified in this tax invoice is made by Me/us and that the transaction of the sale covered by this tax invoice has been effected by Me/Us. And it shall be accounted for in the turnover of sales while filing of return and the due tax,if any payable on the sale has been paid or shall be paid.</b>
                            </td>
                            <td style="word-wrap: break-word;font-size: small" width="100%;"  class="flexibleContainerCell" colspan="2">
SUBJECT TOKHED JURISDICTION If at Anytime the company shall be held liable to any state & Central Sales Tax in respect of this sales such tax will be covered from you
                                <tr>
                                  <td colspan="2" style="word-wrap: break-word;font-size: small">VATTINNO.:27880333241<br/> VDt.01-04-2006<br/> CSTTINNO.:27880333241<br/> CDt.01--2006 <br/>PANNO.: AABPW6443Q</td>
                                </tr>
                            </td>
                          </tr>
                        </table>
                        <!-- // FLEXIBLE CONTAINER -->
                      </td>
                    </tr>
                  </table>
                  <!-- // CENTERING TABLE -->
                </td>
              </tr>
              <!-- // MODULE ROW -->

                            <!-- MODULE ROW // -->
              <tr>
                <td align="center" valign="top">
                  <!-- CENTERING TABLE // -->
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <!-- FLEXIBLE CONTAINER // -->
                        <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td align="center" valign="top" width="500" class="flexibleContainerCell">
                              <table border="0" cellpadding="30" cellspacing="0" width="100%">
                                <tr>
                                  <td align="center" valign="top">

                                    <!-- CONTENT TABLE // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                      <tr>
                                        <td valign="top" class="textContent">
                                          <h3 style="color:#5F5F5F;line-height:125%;font-family:Helvetica,Arial,sans-serif;font-size:20px;font-weight:normal;margin-top:0;margin-bottom:3px;text-align:left;"></h3>
                                          <div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">This is an auto-generated email. Please do not reply. </div>
                                        </td>
                                      </tr>
                                    </table>
                                    <!-- // CONTENT TABLE -->

                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <!-- // FLEXIBLE CONTAINER -->
                      </td>
                    </tr>
                  </table>
                  <!-- // CENTERING TABLE -->
                </td>
              </tr>
              <!-- // MODULE ROW -->
                            <!-- MODULE DIVIDER // -->
              <tr>
                <td align="center" valign="top">
                  <!-- CENTERING TABLE // -->
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <!-- FLEXIBLE CONTAINER // -->
                        <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td align="center" valign="top" width="500" class="flexibleContainerCell">
                              <table class="flexibleContainerCellDivider" border="0" cellpadding="30" cellspacing="0" width="100%">
                                <tr>
                                  <td align="center" valign="top" style="padding-top:0px;padding-bottom:0px;">

                                    <!-- CONTENT TABLE // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                      <tr>
                                        <td align="center" valign="top" style="border-top:1px solid #C8C8C8;"></td>
                                      </tr>
                                    </table>
                                    <!-- // CONTENT TABLE -->

                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <!-- // FLEXIBLE CONTAINER -->
                      </td>
                    </tr>
                  </table>
                  <!-- // CENTERING TABLE -->
                </td>
              </tr>
              <!-- // END -->


              <!-- MODULE ROW // -->
              <tr>
                <td align="center" valign="top">
                  <!-- CENTERING TABLE // -->
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <!-- FLEXIBLE CONTAINER // -->
                        <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td align="center" valign="top" width="500" class="flexibleContainerCell">
                              <table border="0" cellpadding="30" cellspacing="0" width="100%">
                                <tr>
                                  <td align="center" valign="top">

                                    <!-- CONTENT TABLE // -->
                                    <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                      <tr>
                                        <td valign="top" class="textContent">
                                                                                    <div style="text-align:center;font-family:Helvetica,Arial,sans-serif;font-size:15px;margin-bottom:0;margin-top:3px;color:#5F5F5F;line-height:135%;">Contact Us: <a href="mailto:info@ert.com">info@ert.com</a> or Call us <a href="tel:+919922919009">919922919009</a></div>
                                        </td>
                                      </tr>
                                    </table>
                                    <!-- // CONTENT TABLE -->

                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <!-- // FLEXIBLE CONTAINER -->
                      </td>
                    </tr>
                  </table>
                  <!-- // CENTERING TABLE -->
                </td>
              </tr>
              <!-- // MODULE ROW -->

            </table>
            <!-- // END -->

            <!-- EMAIL FOOTER // -->
            <!--
              The table "emailBody" is the email's container.
              Its width can be set to 100% for a color band
              that spans the width of the page.
            -->
            <table bgcolor="#E1E1E1" border="0" cellpadding="0" cellspacing="0" width="500" id="emailFooter">

              <!-- FOOTER ROW // -->
              <!--
                To move or duplicate any of the design patterns
                in this email, simply move or copy the entire
                MODULE ROW section for each content block.
              -->
              <tr>
                <td align="center" valign="top">
                  <!-- CENTERING TABLE // -->
                  <table border="0" cellpadding="0" cellspacing="0" width="100%">
                    <tr>
                      <td align="center" valign="top">
                        <!-- FLEXIBLE CONTAINER // -->
                        <table border="0" cellpadding="0" cellspacing="0" width="500" class="flexibleContainer">
                          <tr>
                            <td align="center" valign="top" width="500" class="flexibleContainerCell">
                              <table border="0" cellpadding="30" cellspacing="0" width="100%">
                                <tr>
                                  <td valign="top" bgcolor="#E1E1E1">

                                    <div style="font-family:Helvetica,Arial,sans-serif;font-size:13px;color:#828282;text-align:center;line-height:120%;">
                                      <div>Copyright &#169; 2020 <a href="https://google.com/auth/login" target="_blank" style="text-decoration:none;color:#828282;"><span style="color:#828282;">ERT India Private Limited.</span></a> All rights reserved.</div>
                                      <div></div>
                                    </div>

                                  </td>
                                </tr>
                              </table>
                            </td>
                          </tr>
                        </table>
                        <!-- // FLEXIBLE CONTAINER -->
                      </td>
                    </tr>
                  </table>
                  <!-- // CENTERING TABLE -->
                </td>
              </tr>

            </table>
            <!-- // END -->

          </td>
        </tr>
      </table>
    </center>
  </body>
</html>

'''
